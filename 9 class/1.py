# 1. Написать класс Car
# Конструктор класса принимает атрибуты:
# color: str (цвет)
# count_passenger_seats: int (количество пассажирских мест)
# is_baby_seat: bool (наличие десткого кресла)
# is_busy: bool (определяется внутри конструктора со значением False, не принимается на
# вход)
# 1.1 Написать магический метод __str__ выводящий форматированную строку с информацией
# об автомобиле

class Car:
    def __init__(self, color: str, count_passanger_seats: int, is_baby_seat: bool, is_busy: bool = False) -> None:
        self.is_busy = is_busy
        self.is_baby_seat = is_baby_seat
        self.color = color
        self.count_passanger_seats = count_passanger_seats

    def __str__(self) -> str:
        baby_seat = ''
        if self.is_baby_seat == False:
            baby_seat = 'without'
        else:
            baby_seat = 'with'
        av = ''
        if self.is_busy == False:
            av = 'avaliable'
        else:
            av = 'NOT avaliable'
        return f'{self.color} auto, {self.count_passanger_seats} seats, {baby_seat} baby seat, {av} now'


test = Car('red', 4, False, True)
print(test.__str__())
