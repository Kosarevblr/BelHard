# Вывести первые N цисел кратные M и больше K


n, m, k = int(input('Vvedi n: ')), int(input('Vvedi m: ')), int(input('Vvedi k: '))
numb = 0
ans = []

while len(ans) < n:
    if numb % m == 0 and numb > k:
        ans.append(numb)
    numb+=1

print(*ans)
