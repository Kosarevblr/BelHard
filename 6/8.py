# Дан словарь, ключ - Название страны, значение - список городов, на вход
# поступает город, необходимо сказать из какой он страны

dict = {'Belarus': 'Minsk', 'Poland': 'Warsaw', 'USA': 'Portland'}
city = input('Enter the city: ')


def opred(dict, city):
    for key, val in dict.items():
        if val == city:
            return key


print(opred(dict, city))


