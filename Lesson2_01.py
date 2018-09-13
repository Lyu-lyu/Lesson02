age = input ('Введите Ваш возраст: ')


def business(age):
    age = int(age)
    occupations_list = ['детский сад', 'школа', 'ВУЗ', 'работа', 'пенсия']

    if age < 7:
        return occupations_list[0]

    elif age < 17:
        return occupations_list[1]

    elif age < 21:
   	    return occupations_list[2]

    elif age < 65:
        return occupations_list[3]

    else:
        return 'Пенсии скоро отменят. Пока-пока!'

occupation = business(age)
print (occupation)