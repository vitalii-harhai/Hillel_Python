LETTER_TEMPLATE = """
Шановний FIRST_NAME_RECIPIENT LAST_NAME_RECIPIENT!
Хочемо запропонувати вам співпрацю з нашою компанією в якості представника у вашому регіоні. 
Ми гарантуємо вам цікаву роботу і високий дохід. Наша пропозиція включає в себе: 
- короткий курс практичного навчання з наданням спеціальної літератури, 
- можливість індивідуального підходу до клієнтів за рахунок великої кількості різноманітних пропозицій, акцій та знижок, 
- допомога з просуванням на ринку. 
Особисто Вам ми гарантуємо високий «агентський» відсоток, а також придбання нашої продукції на більш цікавих умовах.

З повагою, POST_SENDER FIRST_NAME_SENDER LAST_NAME_SENDER. 
"""


def user_letter(first_name_recipient: str,
                last_name_recipient: str,
                first_name_sender: str,
                last_name_sender: str,
                post_sender: str):
    letter = LETTER_TEMPLATE
    letter = letter.replace("FIRST_NAME_RECIPIENT", first_name_recipient)
    letter = letter.replace("LAST_NAME_RECIPIENT", last_name_recipient)
    letter = letter.replace("FIRST_NAME_SENDER", first_name_sender)
    letter = letter.replace("LAST_NAME_SENDER", last_name_sender)
    letter = letter.replace("POST_SENDER", post_sender)

    print(letter)


first_name_r = input("Введіть ім'я одержувача ").capitalize()
last_name_r = input("Введіть прізвище одержувача ").capitalize()
first_name_s = input("Введіть ім'я відправника ").capitalize()
last_name_s = input("Введіть прізвище відправника ").capitalize()
post_s = input("Введіть посаду відправника ").lower()

user_letter(first_name_r, last_name_r, first_name_s, last_name_s, post_s)
