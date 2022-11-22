# 3. Написать класс Numbers
# Конструктор класса принимает список чисел numbers: list[int]
# Написать метод average — возвращающий среднее арифметическое между всеми числами
# Написать метод max_count — возвращающий число из списка, которое чаще встречается,
# если таких чисел несколько, вывести среднее арифметическое среди таких чисел



spis = [1, 2, 3, 4, 5, 5,5, 5, 5, 1, 1, 1, 6, 1, 2, 3, 3]


class numbers:
    def __init__(self, spis: list[int]) -> None:
        self.spis = spis

    def average(self) -> float:
        su = 0
        for i in spis:
            su += i
        return round(su / len(spis), 2)

    def max_count(self) -> int | float:
        from collections import Counter
        result = Counter(spis).most_common()
        s=[]
        for i in range(len(result)):
            s.append(list(result[i]))
        for j in range(len(result)):
            s[j].reverse()
        count = 0
        summa = 0
        for k in range(len(s)):
            if s[k][0] == s[0][0]:
                count+=1
                summa+=s[k][1]

        if count ==0:
            return s[0][1]

        return summa/count



print(numbers.average(spis))
print(numbers.max_count(spis))

# for i in range(len(result)):
#     if result[i][1] is max(result):
#         return result[i][0]
# [[6, 1], [4, 5], [3, 3], [2, 2], [1, 4], [1, 6]]