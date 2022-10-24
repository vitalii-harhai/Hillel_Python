import math


class Triangle:

    def __init__(self, a: float, b: float, c: float):
        #  стороны треугольника
        self.a = self.verification_input_value(a)
        self.b = self.verification_input_value(b)
        self.c = self.verification_input_value(c)
        #  угол A в градусах, если нет треугольника - None
        self.angle_a_degree = self.get_angle_a_degree(output_string=False) if self.exists(output_string=False) else None
        #  угол B в градусах, если нет треугольника - None
        self.angle_b_degree = self.get_angle_b_degree(output_string=False) if self.exists(output_string=False) else None
        # угол C в градусах, если нет треугольника - None
        self.angle_c_degree = self.get_angle_c_degree(output_string=False) if self.exists(output_string=False) else None
        #  тип треугольника по величине углов, если нет треугольника - None
        self.type_angle = self.get_type_angle_value() if self.exists(output_string=False) else None
        #  тип треугольника по числу равных сторон, если нет треугольника - None
        self.type_sides = self.get_type_number_of_sides() if self.exists(output_string=False) else None
        #  площадь треугольника, если нет треугольника - значение None
        self.square = self.get_square(output_string=False) if self.exists(output_string=False) else None
        #  периметр треугольника, если нет треугольника - None
        self.perimeter = self.get_perimeter(output_string=False) if self.exists(output_string=False) else None

    @staticmethod
    def is_triangle(a: float, b: float, c: float) -> int or float:
        """
        Проверяем существование треугольника по сторонам
        :param a: сторона a треугольника
        :param b: сторона b треугольника
        :param c: сторона c треугольника
        :return: сообщение о существовании (если входные данные int или float), None (если входные данные другие)
        """
        try:
            if a < b + c and b < c + a and c < a + b:
                print(f"Трикутник зі сторонами {a}, {b} та {c} це дійсно трикутник, який існує")
            else:
                print(f"Трикутника зі сторонами {a}, {b} та {c} не існує")
        except TypeError:
            return None

    @staticmethod
    def help_create(a: int or float, b: int or float) -> int or float:
        """
        Помогает вычислить третью сторону треугольника при введенных двух сторонах
        :param a: сторона a треугольника
        :param b: сторона b треугольника
        :return: интервал размера третьей стороны
        """
        if a and b:
            print(f'В треугольнике со сторонами a = {a}, b = {b} третья сторона c должна быть в пределах 0 < {a + b}')
        else:
            return None

    @staticmethod
    def verification_input_value(input_value: int or float) -> int or float:
        """
        Проверяет корректность входных данных
        :param input_value: ожидается значение стороны треугольника int или float
        :return: возвращаем то же значение, а если некорректные данные - 0
        """
        if type(input_value) == int or type(input_value) == float:
            return input_value
        else:
            return 0

    def exists(self, output_string=True):
        """
        Проверяем существование треугольника по сторонам
        Для программы возвращаем строку с сообщением, а для класса - bool
        :param output_string: флаг True - возвращаем строку, False - возвращаем bool
        :return: сообщение о существовании треугольника или bool
        """
        if self.a < self.b + self.c and self.b < self.c + self.a and self.c < self.a + self.b:
            if output_string:
                return f"Трикутник зі сторонами {self.a}, {self.b} та {self.c} це дійсно трикутник, який існує"
            else:
                return True
        else:
            if output_string:
                return f"Трикутника зі сторонами {self.a}, {self.b} та {self.c} не існує"
            else:
                return False

    def get_angle_a_degree(self, output_string=True):
        """
        Вычисляем угол А в градусах
        Для программы возвращаем строку с сообщением, а для класса - значение угла
        Если треугольника не существует возвращаем строку с ошибкой или None
        :param output_string: флаг True - возвращаем строку, False - возвращаем значение угла
        :return: строка со значением угла A или значение, если нет треугольника - строка с ошибкой или None
        """
        if self.exists(output_string=False):
            cos_a = (self.b ** 2 + self.c ** 2 - self.a ** 2) / (2 * self.b * self.c)
            a_radians = math.acos(cos_a)
            a_degree = round(math.degrees(a_radians))
            if output_string:
                return f"Угол А дорівнює {a_degree}\u00b0"
            else:
                return a_degree
        else:
            if output_string:
                return 'Цього трикутника не існує, тому у нього не може бути углів!'
            else:
                return None

    def get_angle_b_degree(self, output_string=True):
        """
        Вычисляем угол B в градусах
        Для программы возвращаем строку с сообщением, а для класса - значение угла
        Если треугольника не существует возвращаем строку с ошибкой или None
        :param output_string: флаг True - возвращаем строку, False - возвращаем значение угла
        :return: строка со значением угла B или значение, если нет треугольника - строка с ошибкой или None
        """
        if self.exists(output_string=False):
            cos_b = (self.a ** 2 + self.c ** 2 - self.b ** 2) / (2 * self.a * self.c)
            b_radians = math.acos(cos_b)
            b_degree = round(math.degrees(b_radians))
            if output_string:
                return f"Угол B дорівнює {b_degree}\u00b0"
            else:
                return b_degree
        else:
            if output_string:
                return 'Цього трикутника не існує, тому у нього не може бути углів!'
            else:
                return None

    def get_angle_c_degree(self, output_string=True):
        """
        Вычисляем угол C в градусах
        Для программы возвращаем строку с сообщением, а для класса - значение угла
        Если треугольника не существует возвращаем строку с ошибкой или None
        :param output_string: флаг True - возвращаем строку, False - возвращаем значение угла
        :return: строка со значением угла C или значение, если нет треугольника - строка с ошибкой или None
        """
        if self.exists(output_string=False):
            cos_c = (self.a ** 2 + self.b ** 2 - self.c ** 2) / (2 * self.a * self.b)
            c_radians = math.acos(cos_c)
            c_degree = round(math.degrees(c_radians))
            if output_string:
                return f"Угол C дорівнює {c_degree}\u00b0"
            else:
                return c_degree
        else:
            if output_string:
                return 'Цього трикутника не існує, тому у нього не може бути углів!'
            else:
                return None

    def get_perimeter(self, output_string=True) -> str or float:
        """
        Вычисляем периметр треугольника
        Для программы возвращаем строку с сообщением, а для класса - значение периметра
        Если треугольника не существует возвращаем строку с ошибкой или None
        :param output_string: флаг True - возвращаем строку, False - возвращаем значение периметра
        :return: строка со значением периметра или значение, если нет треугольника - строка с ошибкой или None
        """
        if self.exists(output_string=False):
            perimeter = self.a + self.b + self.c
            if output_string:
                return f"Периметр трикутника дорівнює {perimeter}"
            else:
                return perimeter
        else:
            if output_string:
                return 'Цього трикутника не існує, тому у нього не може бути периметра!'
            else:
                return None

    def get_square(self, output_string=True) -> str or float:
        """
        Вычисляем площадь треугольника
        Для программы возвращаем строку с сообщением, а для класса - значение площади
        Если треугольника не существует возвращаем строку с ошибкой или None
        :param output_string: флаг True - возвращаем строку, False - возвращаем значение площади
        :return: строка со значением площади или значение, если нет треугольника - строка с ошибкой или None
        """
        if self.exists(output_string=False):
            p_per = (self.a + self.b + self.c) / 2
            temp_p = p_per * (p_per - self.a) * (p_per - self.b) * (p_per - self.c)
            square = round(math.sqrt(temp_p), 2)
            if output_string:
                return f"Площа трикутника дорівнює {square}"
            else:
                return square
        else:
            if output_string:
                return 'Цього трикутника не існує, тому у нього не може бути площі!'
            else:
                return None

    def get_type_angle_value(self) -> str:
        """
        Определяем тип треугольника по величине углов
        Если треугольника не существует возвращаем строку с ошибкой
        :return: строка с типом треугольника или строка с ошибкой
        """
        if self.exists(output_string=False):
            if self.angle_a_degree == 90 or self.angle_b_degree == 90 or self.angle_c_degree == 90:
                return 'прямоугольный'
            elif self.angle_a_degree > 90 or self.angle_b_degree > 90 or self.angle_c_degree > 90:
                return 'тупоугольный'
            else:
                return 'остроугольный'
        else:
            return 'Цього трикутника не існує, тому і типу за углами немає'

    def get_type_number_of_sides(self) -> str:
        """
        Определяем тип треугольника по числу равных сторон
        Если треугольника не существует возвращаем строку с ошибкой
        :return: строка с типом треугольника или строка с ошибкой
        """
        if self.exists(output_string=False):
            if self.a == self.b == self.c:
                return 'равносторонний'
            elif self.a == self.b or self.b == self.c or self.a == self.c:
                return 'равнобедренный'
            else:
                return 'разносторонний'
        else:
            return 'Цього трикутника не існує, тому і типу за сторонами немає'

    def __str__(self) -> str:
        """
        Переопределяем встроенное строковое представление треугольника
        Если треугольника не существует возвращаем строку с ошибкой
        :return: строка с вычисляемыми значениями треугольника
        """
        if self.exists(output_string=False):
            return f"Трикутник зі сторонами a - {self.a}, b - {self.b}, c - {self.c} це {self.type_angle} " \
                f"{self.type_sides} трикутник з кутами A - {self.angle_a_degree}\u00b0, " \
                   f"B - {self.angle_b_degree}\u00b0, C - {self.angle_c_degree}\u00b0. Цей трикутник має периметр - " \
                   f"{self.perimeter} та площу - {self.square}."
        else:
            return f"Це неіснуючий трикутник зі сторонами a - {self.a}, b - {self.b}, c - {self.c}"


if __name__ == "__main__":
    #  статические методы класса
    print("*" * 20, 'Методы класса', "*" * 20)
    print('-' * 40)
    print('help_create() помогает вычислить сторону c, передав ему a и b')
    Triangle.help_create(10.4, 15.2)
    print('-' * 40)

    print('is_triangle() выводит сообщение существует ли треугольник')
    Triangle.is_triangle(10, 10, 10)
    Triangle.is_triangle(4, 10, 20)
    print('-' * 40)

    #  создание экземпляров класса
    triangle_1 = Triangle(25, 25, 25)  # остроугольный равносторонний
    triangle_2 = Triangle(25, 20, 40)  # тупоугольный разносторонний
    triangle_3 = Triangle(10, 20, 50)  # не существует
    triangle_4 = Triangle(45, 45, 5)  # остроугольный равнобедренный
    triangle_5 = Triangle('as1', [1, 2, 2], (2, 's'))  # вводим неправильные данные

    #  методы экземпляра
    print("*" * 20, 'Методы экземпляра', "*" * 20)
    print('-' * 40)
    print('__str__() выводит строковое представление треугольника')
    print('triangle_1 ', triangle_1.__str__())
    print('triangle_2 ', Triangle.__str__(triangle_2))
    print('triangle_3 ', triangle_3.__str__())
    print('triangle_4 ', triangle_4.__str__())
    print('triangle_5 ', triangle_5.__str__())

    print('-' * 40)
    print('get_perimeter() выводит значение периметра треугольника')
    print('triangle_1', triangle_1.get_perimeter())
    print('triangle_2', Triangle.get_perimeter(triangle_2))
    print('triangle_3', triangle_3.get_perimeter())
    print('triangle_4', triangle_4.get_perimeter())
    print('triangle_5', triangle_5.get_perimeter())

    print('-' * 40)
    print('get_square() выводит значение площади треугольника')
    print('triangle_1', triangle_1.get_square())
    print('triangle_2', Triangle.get_square(triangle_2))
    print('triangle_3', triangle_3.get_square())
    print('triangle_4', triangle_4.get_square())
    print('triangle_5', triangle_5.get_square())

    print('-' * 40)
    print('exists() выводит сообщение о существовании треугольника')
    print('triangle_1', triangle_1.exists())
    print('triangle_2', Triangle.exists(triangle_2))
    print('triangle_3', triangle_3.exists())
    print('triangle_4', triangle_4.exists())
    print('triangle_5', triangle_5.exists())

    print('-' * 40)
    print('обращение к другим методам')
    print('triangle_1', triangle_1.get_angle_a_degree())
    print('triangle_2', Triangle.get_type_angle_value(triangle_2))
    print('triangle_3', triangle_3.get_type_number_of_sides())
    print('triangle_4', triangle_4.square)
    print('triangle_5', Triangle.get_angle_c_degree(triangle_5))
