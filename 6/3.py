# Дан список чисел и на вход поступает число N, необходимо сместить список на
# указанное число, пример: [1,2,3,4,5,6,7] N=3 ответ: [5,6,7,1,2,3,4]

spis = [i for i in range(0, 30)]
n = int(input('Enter n: '))


def sdvig(n):
    for i in range(0, n + 1):
        a = spis.pop(0)
        spis.append(a)
    return spis


print(sdvig(n))
