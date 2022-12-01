# 2. В файле записано стихотворение. Выведите его на экран, а также
# укажите, каких слов в нем больше: начинающихся на гласную или на
# согласную букву (без учета регистра)?


file = open('text.txt', 'r', encoding='utf-8')
text = file.read()
file = open('text.txt', 'r', encoding='utf-8')
text3 = ' '.join([line.strip() for line in file if line.strip()])
text4 = text3.split()

prim = ['а', 'у', 'ы', 'е', 'о', 'э', 'я', 'и', 'ю']
count1, count2 = 0, 0
for i in range(0, len(text4)):
    if text4[i][0].lower() in prim:
        count1+=1
    else:
        count2+=1

file.close()
print(*['Гласных больше' if count1>count2 else 'Согласных больше'])
