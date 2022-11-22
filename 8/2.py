# 2. Написать класс Rectangle
# Конструктор класса принимает координаты точек по диагонали (правая нижняя, верхняя
# левая или левая нижняя, правая верхняя)
# Написать метод perimeter возвращающий периметр получившегося прямоугольника
# Написать метод square возвращающий площадь получившегося прямоугольникаы
# *учесть, что координаты на плоскости могут быть отрицательными


ax = 2
ay = -1
bx = -1
by = 4

class Restangle:
    def __init__(self, ax:int, ay:int, bx:int, by:int) -> None:
        self.ax = ax
        self.bx = bx
        self.ay = ay
        self.by = by

    @staticmethod
    def perimetr(ax:int, ay:int, bx:int, by:int) -> int:
        return (abs(ax-bx) + abs(ay-by))*2

    @staticmethod
    def sqare(ax:int, ay:int, bx:int, by:int) -> int:
        return abs(ax - bx)*abs(ay-by)

print(Restangle.perimetr(ax, ay, bx, by))
print(Restangle.sqare(ax, ay, bx, by))