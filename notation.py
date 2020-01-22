number_1 = input()
number_1 = number_1.split()

assert (number_1[0] == '+' or number_1[0] == '-' or number_1[0] == '*' or number_1[0] == '/'), 'Недоступная операция'


try:
    if number_1[0] == '+':
        print(int(number_1[1]) + int(number_1[2]))
    elif number_1[0] == '-':
        print(int(number_1[1]) - int(number_1[2]))
    elif number_1[0] == '*':
        print(int(number_1[1]) * int(number_1[2]))
    elif number_1[0] == '/':
        try:
            print(int(number_1[1]) / int(number_1[2]))
        except ValueError:
            print('Строки делить нельзя!')
except ZeroDivisionError:
    print('На ноль делить нельзя!')
except IndexError:
    print('Передано неправильное количество аргументов!')

print('Выполнено')
