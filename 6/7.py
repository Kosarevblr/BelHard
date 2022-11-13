# Дан список чисел, необходимо для каждого элемента посчитать сумму его
# соседей, для крайних чисел одним из соседей является число с противоположной
# стороны списка

lst = [4, 3, 5, 6, 9, 22, 5, 34, 65, 11, 87, 0]

def kr_sum(lst):
    lst_fin = []
    first_s = lst[1] + lst[-1]
    last_s = lst[-2] + lst[0]
    lst_fin.append(first_s)
    for i in range(1, len(lst)-1):
        summa = lst[i-1] + lst[i+1]
        lst_fin.append(summa)
    lst_fin.append(last_s)
    return print(lst_fin)

kr_sum(lst)
