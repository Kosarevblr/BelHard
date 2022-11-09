#Вывести четные числа от 2 до N по 5 в строку

n = int(input("Vvedi n: "))
ves = []
for i in range(2,n+1):
    if i % 2 ==0:
        ves.append(i)


print(*[ves[i:i+5] for i in range(0, len(ves), 5)], sep='\n')
