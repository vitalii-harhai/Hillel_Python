user_list = []


def command_add():
    note = input('Enter your note ')
    length = len(note)
    user_list.append([note, length])


def command_earliest():
    if user_list:
        for i in user_list:
            print(i[0])
    else:
        print("Список нотаток порожній!")


def command_latest():
    if user_list:
        for i in range(1, len(user_list) + 1):
            print(user_list[0 - i][0])
    else:
        print("Список нотаток порожній!")


def command_shortest():
    if user_list:
        sorted_user_list = sorted(user_list, key=lambda it: it[1])
        for i in sorted_user_list:
            print(i[0])
    else:
        print("Список нотаток порожній!")


def command_longest():
    if user_list:
        sorted_user_list = sorted(user_list, key=lambda it: -it[1])
        for i in sorted_user_list:
            print(i[0])
    else:
        print("Список нотаток порожній!")


def command_help():
    print("add - додати нотатку\n"
          "earliest - виводить збережені нотатки у хронологічному порядку - від найранішої до найпізнішої\n"
          "latest - виводить збережені нотатки у хронологічному порядку - від найпізнішої до найранішої\n"
          "longest - виводить збережені нотатки у порядку їх довжини - від найдовшої до найкоротшої\n"
          "shortest - виводить збережені нотатки у порядку їх довжини - від найкоротшої до найдовшої\n"
          "delete - стерти всі нотатки\n"
          "exit - вихід з програми")


def command_delete():
    user_list.clear()
    print("Список нотаток порожній!")


while True:
    command = input('Enter the command (help - get help) ')
    if command.lower() == 'add':
        command_add()
    elif command.lower() == 'earliest':
        command_earliest()
    elif command.lower() == 'latest':
        command_latest()
    elif command.lower() == 'shortest':
        command_shortest()
    elif command.lower() == 'longest':
        command_longest()
    elif command.lower() == 'help':
        command_help()
    elif command.lower() == 'delete':
        command_delete()
    elif command.lower() == 'exit':
        break
    else:
        print('Command not found!')
