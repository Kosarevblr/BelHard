# Пользователь вводит предложение, заменить все пробелы на "-" 2-мя
# способами

#1
text = input()
print(text.replace(' ', '-'))

#2
text = input()
spis = text.split(' ')
print('-'.join(spis))

