a = input ('Введите значение а:')
b = input ('Введите значение b:')

def function(a, b):
    if not (isinstance(a, str) and isinstance(b, str)):
        return 0 
    
    elif a == b:
        return 1

    elif len(a) > len(b):
        return 2 

    elif not (a == b) and b == 'learn':
        return 3
    else:
        return 'Введены неверные данные'
main = function(a, b)
print(main)