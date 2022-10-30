def input_user_number() -> str:
    """
    Принимает от пользователя только целые числа
    """
    while True:
        number = input("Введіть ціле число ")
        try:
            int(number)
            return str(number)
        except ValueError:
            pass


def input_user_characters() -> int:
    """
    Принимает от пользователя только натуральные числа (целые положительные)
    """
    while True:
        characters = input("Введіть кількість символів, які необхідно відрізати з права ")
        if characters.isnumeric():
            return int(characters)


def cut_user_number(number: str, character: int) -> str:
    """
    Возвращает срез из последних character символов числа пользователя number
    Если number отрицательное - убирает знак минус
    """
    number = str(abs(int(number)))
    start = len(number) - character if character <= len(number) else 0
    cut = number[start:]
    return cut


user_number = input_user_number()
user_characters = input_user_characters()
user_cut_number = cut_user_number(user_number, user_characters)
print(f"Останні {user_characters} цифри вашого числа {user_number} це {user_cut_number}")
