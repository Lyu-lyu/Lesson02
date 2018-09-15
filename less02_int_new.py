x = input ('Введите Х:')
y = input ('Введите Y:')

def get_sum (x, y):
    
    try: 
        x = int(x)
        y = int(y)
        summ = x + y
        return summ

    except ValueError:
        print ('Введены неверные данные!')
               
Result = get_sum (x, y)
if Result != None:
    print ('Сумма', Result)