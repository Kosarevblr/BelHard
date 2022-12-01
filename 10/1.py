# 1. Дан многострочный файл txt
# а) разбить файл на N(вводится с клавиатуры) файлов построчно
# б) разбить файл на несколько файлов по N строк

n = int(input('N for A'))
m = int(input('N for B'))
file = open('text.txt', 'r', encoding='utf-8')
count = 0
lines = file.readlines()
file = open('text.txt', 'r', encoding='utf-8')
for line in file:
    count += 1
if count >= n:
    for i in range(1, n + 1):
        new_text_A = lines[i-1]
        new_file_A = f'new1{i}.txt'
        with open(new_file_A, 'w', encoding='utf-8') as file1:
            file1.write(new_text_A)
    for j in range(1, m+1):
        new_text_B = ''.join(lines[:n])
        new_file_B = f'new2{j}.txt'
        with open(new_file_B, 'w', encoding='utf-8') as file2:
            file2.write(new_text_B)

else:
    raise ValueError('too much')
file.close()



