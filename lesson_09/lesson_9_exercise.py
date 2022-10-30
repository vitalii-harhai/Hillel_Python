import json
import uuid


def create_group_list(dbase: list, group: set, sort: str) -> dict:
    """
    Формируем список id записей по группам из set group по полю str
    :param dbase: база данных с индексами в виде списка словарей
    :param group: множество уникальных названий групп
    :param sort: str поле в записи базы данных по которому группируем данные
    :return: словарь key - группа volume - список id записей
    """
    dict_group = dict()
    for g in group:
        volume_list = list()
        for item in dbase:
            if item[sort] == g:
                volume_list.append(item['id'])
        else:
            dict_group.update({g: volume_list})
    return dict_group


##########################################################
"""
Считываем базу данных, добавляем индекс и записываем новый файл json
"""

#  читаем базу данных в формате список словарей
with open('db.json') as f:
    db = json.load(f)

#  перебираем все элементы базы данных и добавляем id
for i in db:
    i.update({'id': str(uuid.uuid1())})

#  записываем проиндексированную базу в файл
index_file = 'db_index.json'
with open(index_file, mode='w') as f:
    json.dump(db, f, indent=4, ensure_ascii=False)

###########################################################
"""
Считываем проиндексированную базу данных, создаем группировки по полям и сохраняем в файлы json
"""
#  читаем проиндексированную базу данных
with open('db_index.json') as f:
    db_index = json.load(f)

#  создаем множества set для определения групп
group_date = set()
group_payment_receiver = set()
group_amount_of_payment = set()
group_payment_currency = set()

#  формируем группы используя особенность set
for i in db_index:
    group_date.add(i['date'])
    group_payment_receiver.add(i['payment receiver'])
    group_amount_of_payment.add(i['amount of payment'])
    group_payment_currency.add(i['payment currency'])

#  формируем словарь key = группа volume = список id относящихся к этой группе с помощью функции
dict_date = create_group_list(db_index, group_date, 'date')
dict_payment_receiver = create_group_list(db_index, group_payment_receiver, 'payment receiver')
dict_amount_of_payment = create_group_list(db_index, group_amount_of_payment, 'amount of payment')
dict_payment_currency = create_group_list(db_index, group_payment_currency, 'payment currency')

#  записываем группы с id в отдельные файлы
files_to_load = {'dict_date.json': dict_date,
                 'dict_payment_receiver.json': dict_payment_receiver,
                 'dict_amount_of_payment.json': dict_amount_of_payment,
                 'dict_payment_currency.json': dict_payment_currency
                 }

for key, volume in files_to_load.items():
    with open(key, mode='w') as f:
        json.dump(volume, f, indent=4, ensure_ascii=False)

##################################################
"""
Выводим сгруппированные данные по группам
"""

#  читаем базу данных
with open('db_index.json') as f:
    db_data_index = json.load(f)

#  выводим отсортированные по группам записи для каждого файла
for key in files_to_load.keys():
    with open(key) as f:
        db_sorted = json.load(f)

    name_group = key.replace('dict_', '-------------------- ')
    name_group = name_group.replace('.json', ' --------------------')
    name_group = name_group.replace('_', ' ')
    print(name_group.upper())

    for key_group, volume_group in db_sorted.items():
        print('group -', key_group)
        for s in volume_group:
            for i in db_data_index:
                if s == i['id']:
                    print(f"---- Date - {i['date']}, name - {i['payment receiver']}, {i['amount of payment']} "
                          f"{i['payment currency']}")
