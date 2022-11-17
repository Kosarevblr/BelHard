# Петя перешёл в другую школу. На уроке физкультуры ему понадобилось определить своё
# место в строю. Помогите ему это сделать. Программа получает на вход невозрастающую
# последовательность натуральных чисел, означающих рост каждого человека в строю. После
# этого вводится число X – рост Пети. Все числа во входных данных натуральные и не
# превышают 200.

rost = list(map(int, input("Enter pupil's growth: ").split()))
petr = int(input('Enter Peters growth: '))

def peters(rost, petr):
    for i in range(len(rost)):
        if rost[i]<petr<rost[i+1]:
            rost.insert(i+1, petr)

    return f"Peter's place - {rost.index(petr)+1}"

print(peters(rost, petr))

