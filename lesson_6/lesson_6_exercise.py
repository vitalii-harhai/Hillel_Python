"""
База данных реализовано в виде 2-х уровневого списка
1 уровень - заметка
2 уровень - текст заметки, ее длина
Для реализации в виде списка словарей
поменять строки 18, 42, 45, 68, 71 на комменты.
"""

user_list = []


def command_add():
    """
    Добавляет заметку в виде списка [текст, длина заметки]
    """
    note = input('Enter your note ')
    length = len(note)
    user_list.append([note, length])  # user_list.append({'note': note, 'length': length})


def command_time(reverse=False):
    """
    Функция сортировки по времени
    Количество выводимых заметок проверяем на положительное число
    Если больше чем в списке элементов, принимаем количество за длину списка
    Старые заметки в начале списка
    От новых к старым - обычный перебор с 0 (старт с 0 вверх)
    От старых к новым - обратный перебор range с шагом -1 (старт с -1 вниз)
    Если список пустой - предупреждение.
    :param reverse: False - от старых к новым, True - от новых к старым.
    :return: Вывод в консоль отсортированные тексты заметок.
    """
    if user_list:
        while True:
            amount_notes = input("Введіть кількість нотаток для перегляду ")
            if amount_notes.isnumeric():
                break
            print("Введіть кількість, тобто додатне число")
        amount_notes = len(user_list) if int(amount_notes) > len(user_list) else int(amount_notes)
        if reverse:
            for i in range(-1, -1 - amount_notes, -1):
                print(user_list[i][0])  # print(user_list[i]['note'])
        else:
            for i in range(amount_notes):
                print(user_list[i][0])  # print(user_list[i]['note'])
    else:
        print("Список нотаток порожній!")


def command_length(reverse=False):
    """
    Функция сортировки по тексту заметки
    Количество выводимых заметок проверяем на положительное число
    Если больше чем в списке элементов, принимаем количество за длину списка
    Отсортированный новый список сортируем lambda по длине заметки
    Если список пустой - предупреждение.
    :param reverse: False - от коротких к длинным, True - от длинных к коротких.
    :return: Вывод в консоль отсортированные тексты заметок.
    """
    if user_list:
        while True:
            amount_notes = input("Введіть кількість нотаток для перегляду ")
            if amount_notes.isnumeric():
                break
            print("Введіть кількість, тобто додатне число")
        amount_notes = len(user_list) if int(amount_notes) > len(user_list) else int(amount_notes)
        if reverse:
            sorted_user_list = sorted(user_list, key=lambda it: -it[1])
            # sorted_user_list = sorted(user_list, key=lambda it: -it['length'])
        else:
            sorted_user_list = sorted(user_list, key=lambda it: it[1])
            # sorted_user_list = sorted(user_list, key=lambda it: it['length'])
        for i in range(amount_notes):
            print(sorted_user_list[i][0])
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
          "delete - стерти всі нотатки\n"
          "exit - вихід з програми")


def command_delete():
    """
    Очищает весь список заметок.
    :return: выводит в консоль сообщение об удалении.
    """
    user_list.clear()
    print("Список нотаток порожній!")


while True:
    command = input('Enter the command (help - get help) ')
    if command.lower() == 'add':
        command_add()
    elif command.lower() == 'earliest':
        command_time()
    elif command.lower() == 'latest':
        command_time(True)
    elif command.lower() == 'shortest':
        command_length()
    elif command.lower() == 'longest':
        command_length(True)
    elif command.lower() == 'help':
        command_help()
    elif command.lower() == 'delete':
        command_delete()
    elif command.lower() == 'exit':
        break
    else:
        print('Command not found! Use help')
