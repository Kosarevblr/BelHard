# 1. Дан многострочный файл txt
# а) разбить файл на N(вводится с клавиатуры) файлов построчно
# б) разбить файл на несколько файлов по N строк

n = int(input())
file = open('text.txt', 'r', encoding='utf-8')
count = 0
lines = file.readlines()
file = open('text.txt', 'r', encoding='utf-8')
for line in file:
    count += 1

if count >= n:
    for i in range(1, n + 1):
        new_text = lines[i-1]
        new_file = f'new{i}.txt'
        with open(new_file, 'w', encoding='utf-8') as file1:
            file1.write(new_text)
else:
    raise ValueError('too much')
file.close()
