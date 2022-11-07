class Product:
    def __init__(self,
                 product_category: str,
                 product_name: str,
                 product_price: float):
        self.product_category = product_category
        self.product_name = product_name
        self.product_price = product_price

    @staticmethod
    def fields():
        return [
            ('product_category', 'категорія продукту'),
            ('product_name', 'назва продукту'),
            ('product_price', 'ціна продукту')
        ]

    def are_you(self, mask: dict) -> bool:
        """
        Получает маску с названием поля (переменной класса) и искомым значением.
        Проверяем каждое значение маски с соответствующей переменной экземпляра
        Если значение маски и значение экземпляра совпадает, добавляем в список проверки True
        Если список проверки содержит только True - экземпляр соответствует маске
        Если список проверки содержит хоть одно False или пустой - экземпляр не соответствует маске
        :param mask: словарь ключ - название поля (переменная класса), значение - искомое значение
        :return: True - эли полностью соответствует маске, False - если нет
        """
        list_bool = []
        for key_mask, volume_mask in mask.items():
            if volume_mask:
                if key_mask in self.__dir__() and self.__getattribute__(key_mask) == volume_mask:
                    yes_its_me = True
                else:
                    yes_its_me = False
                list_bool.append(yes_its_me)
        if False in list_bool or not list_bool:
            return False
        else:
            return True


class Notebook(Product):
    def __init__(self,
                 product_category: str,
                 product_name: str,
                 product_price: float,
                 desktop_os: str,
                 processor: str,
                 ram_size: int):
        super().__init__(product_category, product_name, product_price)
        self.desktop_os = desktop_os
        self.processor = processor
        self.ram_size = ram_size
        self.additional_fields = {"desktop_os": desktop_os, "processor": processor, "ram_size": ram_size}

    def __str__(self):
        """
        Описание экземпляра
        :return: строка с описанием экземпляра
        """
        summary = f'Ноутбук модель {self.product_name}, з ОС {self.desktop_os} ' \
                  f'та процесором {self.processor}, за ціною {self.product_price}'
        return summary


class Smartphone(Product):
    def __init__(self,
                 product_category: str,
                 product_name: str,
                 product_price: float,
                 mobile_os: str,
                 screen_size: float):
        super().__init__(product_category, product_name, product_price)
        self.mobile_os = mobile_os
        self.screen_size = screen_size
        self.additional_fields = {
            'mobile_os': mobile_os,
            'screen_size': screen_size
        }

    def __str__(self):
        """
        Описание экземпляра
        :return: строка с описанием экземпляра
        """
        summary = f'Смартфон модель {self.product_name}, з ОС {self.mobile_os} ' \
                  f'та розміром екрану {self.screen_size}, за ціною {self.product_price}'
        return summary


class Printer(Product):
    def __init__(self,
                 product_category: str,
                 product_name: str,
                 product_price: float,
                 color: str):
        super().__init__(product_category, product_name, product_price)
        self.color = color
        self.additional_fields = {'color': color}

    def __str__(self):
        """
        Описание экземпляра
        :return: строка с описанием экземпляра
        """
        summary = f'Принтер модель {self.product_name}, {self.color}, за ціною {self.product_price}'
        return summary
