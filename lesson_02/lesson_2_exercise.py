"""
5. Написати програму, яка приймає число та повідомляє, яка в ньому остання цифра.
Наприклад: 10 -> 0, 100 -> 0, 25143 -> 3
"""


def function_find_last_number():
    """
    При введенні користувачем позитивного або відʼємного цілого/дробового/комплексного числа
    функція повертає останню цифру
    Функція також видаляє пробіли на початку та вкінці введені строки
    В інших випадках потребує введення іншої спроби, та після третьої спроби завершується
    """
    global attempt_count
    user_number = input('Введіть число: ')
    try:
        float(user_number)
        user_number = user_number.strip()
        find_numeric = user_number[-1]
        print(f'Ви ввели число - {user_number}, остання цифра в ньому - {find_numeric}')
    except ValueError:
        attempt_count += 1
        if attempt_count < 3:
            function_find_last_number()
        else:
            print("Ви ввели три рази неправильно. Програма завершується")


attempt_count = 0

function_find_last_number()
