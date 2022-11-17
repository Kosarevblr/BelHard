# Написать функцию pow, которая принимает число А и число Б, необходимо с помощью
# рекурсии возвести число А в степень Б


a, b = int(input('Enter A: ')), int(input('Enter B: '))

def pow(a, b):
    if b == 0:
        return 1
    if b == 1:
        return a
    if b !=1:
        return a*pow(a, b-1)

print(f'A**B = {pow(a, b)}')