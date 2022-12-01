# 3. Дан файл с текстом, необходимо в проанализировать файл и сказать
# сколько слов и букв в каждой строке

with open('text.txt', 'r', encoding='utf-8') as file:
    text = [line.strip() for line in file if line.strip()]
    for i in range(0, len(text)):
        s = ''.join(text[i])
        prob = s.count(' ')+1
        letter = len(s.replace(' ', ''))
        print(f'В {i} строке {prob} слов и {letter} букв')
