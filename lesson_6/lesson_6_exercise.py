"""
База данных - словарь словарей
key - id заметки str
value - заметка = dict {текст заметки, размер заметки, timestamp создания}
"""

from datetime import datetime
import json
import os
import uuid

DB_FILE = 'db_file.json'


def command_add() -> (str, dict):
    """
    Создает заметку в виде кортежа
    id заметки - используем модуль uuid и формируем с помощью HostID и текущего времени
    :return: кортеж (id заметки, заметка)
    id (str) - id заметки
    note (dict) - {'note': str (текст заметки), 'length': int (вычисляемый размер заметки),
    'date': str (timestamp создания)}
    """
    note = input('Enter your note ')
    date_creation = datetime.now()
    length = len(note)
    note_object = {'note': note, 'length': length, 'date': datetime.timestamp(date_creation)}
    note_id = uuid.uuid1()
    return str(note_id), note_object


def command_sort(db: dict, sort_option: str, reverse=False, get_db=False) -> dict:
    """
    Функция сортировки базы данных
    Количество выводимых заметок проверяем на положительное число
    Если больше чем в списке элементов, принимаем количество за длину списка
    Отсортированный новый список сортируем lambda по ключу сортировки
    Если список пустой - предупреждение.
    :param db: база данных (dict)
    :param sort_option: ключ сортировки str "date"-по дате заметки, "length" - по длине заметки
    :param reverse: сортировка False - от коротких/старых к длинным/новым, True-в обратном порядке
    :param get_db: True - получаем отсортированную базу данных, False - нет
    :return: Вывод в консоль отсортированные тексты заметок, если get_db=True - получаем отсортированную базу данных
    """
    if db:
        if reverse:
            sorted_db_list = sorted(db.items(), key=lambda item: (-item[1][sort_option]))
        else:
            sorted_db_list = sorted(db.items(), key=lambda item: (item[1][sort_option]))
        if get_db:
            return dict(sorted_db_list)
        else:
            while True:
                amount_notes = input("Введіть кількість нотаток для перегляду ")
                if amount_notes.isnumeric():
                    break
                print("Введіть кількість, тобто додатне число")
            amount_notes = len(db) if int(amount_notes) > len(db) else int(amount_notes)
            s = 1
            for key, value in sorted_db_list:
                if s <= amount_notes:
                    print(value['note'])
                s += 1
    else:
        print("Список нотаток порожній!")


def command_help():
    """
    Команда help
    :return: вывод в консоль список всех команд.
    """
    print("add - додати нотатку\n"
          "earliest - виводить збережені нотатки у хронологічному порядку - від найранішої до найпізнішої\n"
          "latest - виводить збережені нотатки у хронологічному порядку - від найпізнішої до найранішої\n"
          "longest - виводить збережені нотатки у порядку їх довжини - від найдовшої до найкоротшої\n"
          "shortest - виводить збережені нотатки у порядку їх довжини - від найкоротшої до найдовшої\n"
          "load - завантажити збережені нотатки зі службового файлу\n"
          "save - зберегти всі активні нотатки у службовий файл\n"
          "clear - видалити всі збережені нотатки та видалити файл зберігання нотаток\n"
          "exit - вихід з програми")


def db_read(file_name: str) -> dict:
    """
    Читаем файл сохраненных заметок
    :param file_name: название файла базы данных
    :return: база данных с файла в виде словаря словарей {id: {note, length, date}}
    """
    try:
        with open(file_name, mode='r') as f:
            db = json.load(f)
    except FileNotFoundError:
        db = dict()
    except json.decoder.JSONDecodeError:  # защита если содержимое файла стереть
        db = dict()
    return db


def db_write(file_name: str, db: dict):
    """
    Записываем базу данных текущих заметок
    :param file_name: название файла базы данных
    :param db: база данных текущих заметок dict
    :return: Если есть какие-то ошибки - выводим их в консоль
    """
    try:
        with open(file_name, mode='w') as file:
            # используем ensure_ascii=False для читабельности кириллицы в json-файле и отступы indent=4
            json.dump(db, file, indent=4, ensure_ascii=False)
    except Exception as error:
        print(error)


db_temp = dict()

while True:
    # в цикле постоянно считываем файл базы данных
    db_saved = db_read(DB_FILE)
    command = input('Enter the command (help - get help) ')
    if command.lower() == 'add':
        add_note = command_add()
        # текущую базу данных заметок обновляем заметкой
        db_temp.update({add_note[0]: add_note[1]})
    elif command.lower() == 'earliest':
        command_sort(db_temp, sort_option='date')
    elif command.lower() == 'latest':
        command_sort(db_temp, sort_option='date', reverse=True)
    elif command.lower() == 'shortest':
        command_sort(db_temp, sort_option='length')
    elif command.lower() == 'longest':
        command_sort(db_temp, sort_option='length', reverse=True)
    elif command.lower() == 'help':
        command_help()
    elif command.lower() == 'save':
        if db_temp:
            # объединяем текущие заметки с сохраненными
            db_temp.update(db_saved)
            # сортируем по дате создания для читабельности файла
            db_temp = command_sort(db_temp, sort_option='date', get_db=True)
            db_write(DB_FILE, db_temp)
            print('Нотатки успішно збережені')
        else:
            print('У вас нема нотаток для збереження')
    elif command.lower() == 'load':
        # если файл с заметками не пустой, объединяем с текущими заметками, иначе - выводим сообщение
        if db_saved:
            db_temp.update(db_saved)
            print('Нотатки успішно завантажено')
        else:
            print('Список нотаток був порожній')
    elif command.lower() == 'clear':
        while True:
            # убеждаемся, что пользователь хочет удалить заметки
            answer = input('Ви впевнені, що хочете видалити всі нотатки? (так-y, ні-n)')
            if answer == 'y':
                if db_temp or os.path.exists(DB_FILE):
                    # если есть текущие заметки - удаляем
                    if db_temp:
                        db_temp.clear()
                        print('Поточні нотатки видалено')
                    # если есть сохраненный файл заметок - удаляем
                    if os.path.exists(DB_FILE):
                        os.remove(DB_FILE)
                        print('Файл зі збереженими нотатками видалено')
                    break
                # в этом случае удалять нечего - выводим сообщение
                if not db_temp and not os.path.exists(DB_FILE):
                    print('Вам нема що видаляти')
                    break
            elif answer == 'n':
                break
    elif command.lower() == 'exit':
        break
    else:
        print('Command not found! Use help')
