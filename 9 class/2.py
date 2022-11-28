# 2. Написать класс Taxi
# Конструктор класса принимает атрибуты:
# cars: list[Car] (список экземпляров класса Car)
# 2.1 Реализовать метод find_car
# На вход метода поступают атрибуты: count_passengers, is_baby (количество пассажиров,
# наличие ребенка, примечание: количество пассажиров с учетом ребенка если он есть)
# На основании данных, вернуть объект Car из атрибута cars подходящий по параметрам и
# свободный (is_busy = False), у автомобиля сменить атрибут is_busy на значение True, если
# подходящего автомобиля нет, метод должен возвращать None

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


test = Car('red', 4, False, False)
print(test.__str__())


class Taxi(Car):
    def __init__(
            self, cars: list[Car], color: str, count_passanger_seats: int, is_baby_seat: bool,
            count_passangers=int, baby_counter: bool = False
    ):
        super().__init__(color, count_passanger_seats, is_baby_seat)
        self.cars = cars
        self.count_passangers = count_passangers
        self.baby_counter = baby_counter

    def find_car(self, count_passangers: int, baby_counter: bool = False,
                 ) -> str:

        for car in list[Car]:
            if Car.count_passanger_seats >= count_passangers or \
                    (baby_counter == True and is_baby_seat == False) or \
                    is_busy == False:
                return car
            else:
                return None


print(Taxi.find_car(5, True))
