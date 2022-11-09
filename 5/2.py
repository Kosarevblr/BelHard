# Сделать калькулятор: у пользователя
# спрашивается число, потом действие и второе
# число

n1, symb, n2 = int(input('Vvedi pervoe 4islo: ')), input('Vvedi znak operatsii: '), int(input('Vvedi vtoroe 4islo: '))
if symb == '+':
    print(n1+n2)
elif symb == '-':
    print(n1-n2)
elif symb == '*':
    print(n1*n2)
elif symb == '/':
    print((n1/n2))
else:
    print('Vvedi "+", "-", "*", "/"')
