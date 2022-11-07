# *Заполнить словарь где ключами будут выступать числа от 0 до n, а
# значениями вложенный словарь с ключами "name" и "email", а значения
# для этих ключей будут браться с клавиатуры

n = int(input('n = '))
nested_dict = {}
nested_dict['name'] = input('name: ')
nested_dict['email'] = input('email: ')
fin = {i: nested_dict for i in range(n)}
print(fin)
