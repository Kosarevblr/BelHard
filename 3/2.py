# Пользователь вводит 3 числа, найти среднее арифмитическое с
# точность 3

a, b, c = int(input()), int(input()), int(input())
sred_ar = (a + b + c)/3
print(round(sred_ar, 3))
