documents = [
    {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
    {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
    {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006', '5400 028765', '5455 002299'],
    '3': []
}


def add_documents(document, directorie):
    number_document = input('Введите номер документа: ')
    type_document = input('Введите тип документа: ')
    name_owner = input('Введите имя владельца: ')
    number_shelf = input('Введите номер полки: ')
    if int(number_shelf) <= len(directorie):
        document.append({'type': type_document, 'number': number_document, 'name': name_owner})
        directorie[number_shelf].append(number_document)
        print('Ваши документы добавлены!')
    else:
        print('Такой полки не существует! Попробуйте ещё раз!')


def shelf_by_number(document):
    number1 = input('Введите номер документа: ')
    for key, value in document.items():
        if number1 in value:
            return key


def list_documents(document):
    for list_document in document:
        print(f'{list_document["type"]} "{list_document["number"]}" "{list_document["name"]}"')


def name_by_number(document):
    number = input('Введите номер документа: ')
    for names in document:
        if number == names['number']:
            return names['name']


def names_owner(document):
    for names in document:
        try:
            print(names['name'])
        except KeyError:
            print('Отсутствует поле "name" у документа!')


def main():
    while True:
        user_input = input('Введите команду: ')
        if user_input == 'p':
            document_owner = name_by_number(documents)
            if document_owner == None:
                print('Документа с таким номером нет в списке!\n'
                      'Если вы хотите добавить документ введите команду "a"')
            else:
                print('Данный документ принадлежит:', document_owner)
        elif user_input == 'l':
            list_documents(documents)
        elif user_input == 's':
            shelf_number = shelf_by_number(directories)
            if shelf_number == None:
                print('Документа с таким номером нет в списке!\n'
                      'Если вы хотите добавить документ введите команду "a"')
            else:
                print('Данный документ находится на полке №', shelf_number)
        elif user_input == 'a':
            add_documents(documents, directories)
        elif user_input == 'o':
            names_owner(documents)
        elif user_input == 'help':
            print('Список команд:\np - поиск человека по номеру документа\n'
                  'l - вывести список всех документов\n'
                  's - узнать номер полки на которой находится документ\n'
                  'a - добавить новый документ в каталог и в перечень полок'
                  '(необходимо указать номер документа, тип, имя владельца и номер полки)\n'
                  'o - вывести список всех владельцев документов\n'
                  'q - выход из программы')
        elif user_input == 'q':
            break
        else:
            print('Такой команды не существует\nПосмотреть полный список команд вы можете набрав слово "help"\n'
                  'Для выхода из программы нажмите "q"')


main()
