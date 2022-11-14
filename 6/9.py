# Дан словарь словарей, ключ внешнего словаря - id пользователя, значение -
# словарь с данными о пользователе (имя, фамилия, телефон, почта), вывести
# имена тех, у кого не указана почта (нет ключа email или значение этого ключа -
# пустая строка)

dict = {1: {'name': 'Magnus', 'last_name': 'Govnuk', 'mob_number': +666666, 'mail': ''},
        2: {'name': 'Bender', 'last_name': 'Rodrigues', 'mob_number': +777777, 'mail': 'lalala@gmail.com'},
        3: {'name': 'Peter', 'last_name': 'Griffin', 'mob_number': +888888, 'mail': None}}

def nomail(dict):
    x=[]
    for i in dict.keys():
        if '' == dict[i]['mail'] or None == dict[i]['mail']:
            x.append(dict[i].get('name'))
    return ', '.join(x)
print(nomail(dict))