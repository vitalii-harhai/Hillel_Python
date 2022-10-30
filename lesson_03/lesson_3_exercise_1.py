user_exit = False

while not user_exit:
    try:
        user_number = int(input("Введіть число: "))

        if user_number <= -500:
            print(f"Ваше число {user_number} в діапазоні ({user_number} <= -500)")
        elif -500 < user_number <= -100:
            print(f"Ваше число {user_number} в діапазоні (-500 < {user_number} <= -100)")
        elif -100 < user_number < 0:
            print(f"Ваше число {user_number} в діапазоні (-100 < {user_number} < 0)")
        elif 0 <= user_number < 100:
            print(f"Ваше число {user_number} в діапазоні (0 <= {user_number} < 100)")
        elif 100 <= user_number < 500:
            print(f"Ваше число {user_number} в діапазоні (100 <= {user_number} < 500)")
        else:
            print(f"Ваше число {user_number} в діапазоні (500 <= {user_number})")

        user_exit = True

    except ValueError:
        print("Ви ввели не число!")
