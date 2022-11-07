import csv
from product import *
from finder import *
from menu import *


def read_csv():
    with open('products.csv', mode='r') as file:
        csv_file = csv.reader(file)
        csv_objects = list()
        for s in csv_file:
            csv_objects.append(s)
    return csv_objects


def get_read_additional_fields(str_csv):
    obj_str = str_csv[3].replace('{', '').replace('}', '').replace(' ', '').replace("'", '')
    obj_str = obj_str.split(',')
    additional_fields = dict()
    for a in obj_str:
        key, value = a.split(':')
        additional_fields.update({key: value})
    return additional_fields


def deserialization(list_csv_lines):
    list_read_objects = list()
    for i in list_csv_lines:
        read_additional_fields = get_read_additional_fields(i)
        if i[0] == 'notebook':
            read_object = Notebook(product_category=i[0], product_name=i[1], product_price=float(i[2]),
                                   desktop_os=read_additional_fields['desktop_os'],
                                   processor=read_additional_fields['processor'],
                                   ram_size=int(read_additional_fields['ram_size']))
        elif i[0] == 'printer':
            read_object = Printer(product_category=i[0], product_name=i[1], product_price=float(i[2]),
                                  color=read_additional_fields['color'])
        elif i[0] == 'smartphone':
            read_object = Smartphone(product_category=i[0], product_name=i[1], product_price=float(i[2]),
                                     mobile_os=read_additional_fields['mobile_os'],
                                     screen_size=float(read_additional_fields['screen_size']))
        else:
            read_object = None
        list_read_objects.append(read_object)
        read_additional_fields.clear()
    return list_read_objects


if __name__ == '__main__':
    read_csv_objects = read_csv()
    list_product_object = deserialization(read_csv_objects)

    mask = dict()
    menu_list = MenuList(list_product_object)

    for item in Product.fields():
        print('Доступні такі категорії пошуку ')
        print(menu_list.field_items(field=item[0], temp_menu=mask))
        mask_item = input(f'пошук по {item[1]} ')
        if mask_item:
            if mask_item.isnumeric():
                mask_item = float(mask_item)
            mask.update({item[0]: mask_item})

    print(mask)
    google = Google(mask, list_product_object).list_sorted_object()
    print('в наявності такі продукти')
    for find_products in google:
        print(find_products.__str__())
