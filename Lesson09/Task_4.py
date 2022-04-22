####################################################################################################################
# Задание 4                                                                                                        #
# Реализуйте базовый класс Car:                                                                                    #
# - у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop,     #
#       turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);              #
# - опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;                                     #
# - добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;              #
# - для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и      #
#       40 (WorkCar) должно выводиться сообщение о превышении скорости.                                            #
####################################################################################################################

class Car():
    def __init__(self, color, name) -> None:
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = False

    def go(self, speed):
        self.speed = speed
        if self.speed == 0:
            print('Машина не может ехать со скоростью 0')
        elif self.speed < 0:
            print('Машина поехала назад')
        else:
            print('Машина поехала')

    def stop(self):
        self.speed = 0
        print('Машина остановилась')

    def turn(self, direction):
        if str.lower(direction) == "лево" or str.lower(direction) == "право":
            if self.speed == 0:
                print('Машина стоит и не может попорачивать')
            elif self.speed < 0:
                print('Машина движется назад и повернула на', direction)
            else:
                print('Машина повернула на', direction)
        else:
            print(
                'Вы задали неверное направление! Укажите направление поворота "лево" или "право".')

    def show_speed(self):
        print('Текущаяя скорость:', self.speed)

    def show_car(self):
        print(
            f'Вы управляете автомобилем: {self.name}. Цвет: {self.color}.')


class TownCar(Car):
    def __init__(self, color, name) -> None:
        super().__init__(color, name)

    def show_speed(self):
        print('Текущаяя скорость:', self.speed)
        if self.speed > 60:
            print('Вы превышаете допустимую скорость 60 км/ч')


class SportCar(Car):
    def __init__(self, color, name) -> None:
        super().__init__(color, name)


class WorkCar(Car):
    def __init__(self, color, name) -> None:
        super().__init__(color, name)

    def show_speed(self):
        print('Текущаяя скорость:', self.speed)
        if self.speed > 40:
            print('Вы превышаете допустимую скорость 40 км/ч')


class PoliceCar(Car):
    def __init__(self, color, name) -> None:
        super().__init__(color, name)
        self.is_police = True

    def show_car(self):
        print(
            f'Вы управляете полицейским автомобилем: {self.name}. Цвет: {self.color}.')


car = Car('Черный', 'Нива')
car.show_car()
car.go(77)
car.show_speed()
car.go(55)
car.turn('лево')
car.stop()
car.show_speed()

print()

bus = TownCar('Зеленый', 'ЛИАЗ')
bus.show_car()
bus.go(77)
bus.show_speed()
bus.go(55)
bus.turn('лево')
bus.stop()
bus.show_speed()

print()

sport = SportCar('Красный', 'Ferrary')
sport.show_car()
sport.go(100)
sport.show_speed()
sport.turn('право')
sport.stop()
sport.show_speed()

print()

gaz = WorkCar('Белый', 'Газель')
gaz.show_car()
gaz.go(77)
gaz.show_speed()
gaz.go(35)
gaz.turn('лево')
gaz.stop()
gaz.show_speed()

print()

pol = PoliceCar('Синий', 'Лада')
pol.show_car()
pol.go(100)
pol.show_speed()
pol.turn('право')
pol.stop()
pol.show_speed()

print()
