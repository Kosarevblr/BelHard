# Дан список чисел, необходимо его развернуть без использования метода revese и
# функции reversed, а так же дополнительного списка и среза

spis = [i for i in range(0, 30)]


def revers(spis):
    m = len(spis)-1
    for i in range(0, len(spis)//2):
        x = spis[m]
        spis[m] = spis[i]
        spis[i] = x
        m -= 1

    return spis


print(revers(spis))

