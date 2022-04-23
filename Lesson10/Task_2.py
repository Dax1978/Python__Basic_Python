####################################################################################################################
# Задание 2                                                                                                        #
# Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность (класс) этого      #
# проекта — одежда, которая может иметь определённое название. К типам одежды в этом проекте относятся пальто и    #
# костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть       #
# обычные числа: V и H соответственно.                                                                             #
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),             #
# для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.                                       #
# Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке знания. Реализовать        #
# абстрактные классы для основных классов проекта и проверить работу декоратора @property.                         #
####################################################################################################################

from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def __init__(self, name) -> None:
        self.name = name

    @property
    @abstractmethod
    def consumption_fabric(self, param):
        pass


class Coat(Clothes):
    def __init__(self, name, size) -> None:
        super().__init__(name)
        self.size = int(size)

    @property
    def consumption_fabric(self):
        return self.size/6.5 + 0.5


class Suit(Clothes):
    def __init__(self, name, height) -> None:
        super().__init__(name)
        self.height = int(height)

    @property
    def consumption_fabric(self):
        return 2 * self.height + 0.3


coat = Coat("Model_coat_1", 52)
print(
    f"Для пошива пальто {coat.name} необходимо {coat.consumption_fabric} ткани.")
suit = Suit("Model_suit_1", 165)
print(
    f"Для пошива костюма {suit.name} необходимо {suit.consumption_fabric} ткани.")
print(f"Для пошива пальто и костюма потребуется",
      coat.consumption_fabric + suit.consumption_fabric, "ткани.")
