summa = 0

while True:
    number = input("Введіть число ")
    if number == "sum":
        print(f"Сума введених чисел дорівнює {str(summa)}")
        break
    else:
        try:
            summa += float(number)
        except ValueError:
            print("Введіть число або sum!")
