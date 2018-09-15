# Напишите функцию get_summ(num_one, num_two), 
# которая принимает на вход два целых числа (int) и складывает их
# Оба аргумента нужно приводить к целому числу при помощи int() и
#  перехватывать исключение ValueError если приведение типов не сработало

x = input ('Введите Х:')
y = input ('Введите Y:')

def get_sum (x, y):
    try:
        x = int(x)
        y = int(y)
        summ = x + y
        return summ
    except ValueError:
        x = input ('Введите Х:')
        y = input ('Введите Y:')
        return get_sum (x, y) 
Result = get_sum (x, y)
print (Result)