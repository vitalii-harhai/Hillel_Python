hello_phrases = ['привіт', 'хай', 'доброго дня']
how_are_you_phrases = ['як справи?', 'що робиш?', 'чим займаєшся?']
films_phrases = ['фільм', 'кінотеатр', 'серіал']
bye_phrases = ['бувай', 'надобраніч', 'гудбай', 'до зустрічі']

print('Бот: Давай поспілкуємося')

while True:
    user_answer = input('Ви: ').lower()
    if user_answer in hello_phrases:
        print("Бот: Доброго вечора, я бот з України!")
    elif user_answer in how_are_you_phrases:
        print("Бот: Вчусь програмувати на Python!")
    elif user_answer in films_phrases:
        print("Бот: Соррі що втручуюсь, не знаю про що йдеться мова, "
              "але подивіться серіал/фільм Термінатор, він просто бомба!")
    elif user_answer in bye_phrases:
        print("Побачимось у мережі, I'll be back.")
        break
    else:
        print("Дуже цікаво, але, нажаль, ніфіга не зрозуміло :( ")
