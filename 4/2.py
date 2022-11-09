# Без использования collections, написать программу, которая будет
# создавать словарь для подсчитывания количества вхождений каждой
# буквы в текст введенный с клавиатуры

n = input().lower()
a = 'abcdefghijklmnopqrstuvwxyz'
keys = dict.fromkeys([a[i] for i in range(len(a))], 0)

b=[(a[i] for i in range(len(n)))]

print(keys)
print(b)