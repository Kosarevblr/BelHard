# Заполнить список степенями числа 2 (от 2^1 до 2^n).

n = int(input('n = '))
s = [2**i for i in range(1, n+1)]
print(s)