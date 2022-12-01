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
    def __init__(self, color: str, count_passanger_seats: int, is_baby_seat: bool) -> None:
        self.is_busy = False
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
        if self.is_busy == True:
            av = 'avaliable'
        else:
            av = 'NOT avaliable'
        return f'{self.color} auto, {self.count_passanger_seats} seats, {baby_seat} baby seat, {av} now'


test = Car('red', 4, False)
# print(test.__str__())


class Taxi:
    def __init__(self, cars: list[Car]) -> None:
        self.cars = cars

    def find_car(self, count_passangers: int, is_baby: bool) -> Car | None:
        for car in self.cars:
            if car.count_passanger_seats >= count_passangers and not car.is_busy:
                if is_baby and car.is_baby_seat:
                    car.is_busy = True
                    return car
                elif not is_baby:
                    car.is_busy = True
                    return car


car1 = Car('white', 4, False)
car2 = Car('red', 6, True)
car3 = Car('white', 5, True)
cars = [car1, car2, car3]
taxi = Taxi(cars)
print(taxi.find_car(5, True))
