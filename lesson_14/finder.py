from product import Product


class Google:
    """
    Механизм поиска по маске
    """
    def __init__(self, mask: dict, list_object: list[Product]):
        self.mask = mask
        self.list_object = list_object

    def list_sorted_object(self) -> list[Product]:
        """
        Перебираем все экземпляры класса Product
        Обращаемся к каждому экземпляру через метод are_you()
        :return: список экземпляров Product, соответствующих маске
        """
        list_sorted_product = []
        for i in self.list_object:
            if i.are_you(mask=self.mask):
                list_sorted_product.append(i)
        return list_sorted_product
