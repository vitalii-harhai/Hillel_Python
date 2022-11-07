from product import Product


class MenuList:
    """
    Экземпляр содержит список объектов класса Product
    """
    def __init__(self, list_object: list[Product]):
        self.list_object = list_object

    def field_items(self, field, temp_menu: dict) -> list[str]:
        """
        Формирует список уникальных значений для меню по маске.
        :param field: поле, по которому отбираем список уникальных значений.
        :param temp_menu: маска, по которой формируем список уникальных значений.
        :return: список list уникальных значений
        """
        field_volume = []
        for i in self.list_object:
            if temp_menu:
                for key_temp_menu, volume_temp_menu in temp_menu.items():
                    if i.__getattribute__(key_temp_menu) == volume_temp_menu:
                        if i.__getattribute__(field) not in field_volume:
                            field_volume.append(i.__getattribute__(field))
            else:
                if i.__getattribute__(field) not in field_volume:
                    field_volume.append(i.__getattribute__(field))
        return field_volume
