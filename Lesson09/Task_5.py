####################################################################################################################
# Задание 5                                                                                                        #
# Реализовать класс Stationery (канцелярская принадлежность):                                                      #
# - определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;#
# - создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);                                   #
# - в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное   #
#       сообщение;                                                                                                 #
# - создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.                    #
####################################################################################################################

# Декоратор для методов draw в Pen, Pencil, Handle
def draw_stationery(func):
    def wrapper(self):
        func(self)
        print(f'Инструмент: {self.title}')
        return func
    return wrapper


class Stationery():
    def __init__(self) -> None:
        self.title = 'Что то общее'

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def __init__(self) -> None:
        super().__init__()
        self.title = 'ручка'

    @draw_stationery
    def draw(self):
        super().draw()


class Pencil(Stationery):
    def __init__(self) -> None:
        super().__init__()
        self.title = 'карандаш'

    @draw_stationery
    def draw(self):
        super().draw()


class Handle(Stationery):
    def __init__(self) -> None:
        super().__init__()
        self.title = 'маркер'

    @draw_stationery
    def draw(self):
        super().draw()


print()

stationery = Stationery()
stationery.draw()

print()

pen = Pen()
pen.draw()

print()

pencil = Pencil()
pencil.draw()

print()

handle = Handle()
handle.draw()

print()
