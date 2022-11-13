# Дан список рандомных чисел, необходимо отсортировать его в виде, сначала
# четные, потом нечётные


lst = [2,5,7,8,0,11,44,55,66,765,332,7,2,3,22]

def sorting(lst):
    a = []
    b = []
    for i in range(0, len(lst)):
        if lst[i] % 2 == 0:
            a.append(lst[i])
        else:
            b.append(lst[i])
    return (a + b)

print(sorting(lst))