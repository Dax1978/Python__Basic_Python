import datetime
from Task_4_5_6_OffiseEquipment import OfficeEquipment


class Copier(OfficeEquipment):
    count = 0

    def __init__(self, brend, model, paper, roll_flat) -> None:
        super().__init__(brend, model)
        self.count += 1
        # Размер листов 1 - A4, 2 - A3, 3 - A2, 4 - A1, 5 - A0
        self.paper = paper
        self.roll_flat = roll_flat

    def __str__(self) -> str:
        str = super().__str__()
        if self.paper == 1:
            str += f"Размер сканируемого листа: A4\n"
        if self.paper == 2:
            str += f"Размер сканируемого листа: A3\n"
        if self.paper == 3:
            str += f"Размер сканируемого листа: A2\n"
        if self.paper == 4:
            str += f"Размер сканируемого листа: A1\n"
        if self.paper == 5:
            str += f"Размер сканируемого листа: A0\n"
        if self.roll_flat == 1:
            str += f"Тип сканера: протяжной"
        if self.roll_flat == 2:
            str += f"Тип сканера: планшетный"
        return str

    # Метод добавления Ксерокса
    @classmethod
    def add(cls):
        brend = input("Укажите бренд ксерокса: ")
        model = input("Укажите модель ксерокса: ")
        paper = cls.int_value(
            "Укажите размер копируемого листа. 1 - А4, 2 - А3, 3 - А2, 4 - А1, 5 - А0: ", 1, 5)
        roll_flat = cls.int_value(
            "Укажите 1 или 2, для протяжного или планшетного ксерокса соответственно: ", 1, 2)
        add_from = input("Укажите откуда прибыл ксерокс на склад: ")
        add_date = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
        el = Copier(brend, model, paper, roll_flat)
        # Откуда поступил на склад
        el.add_from = add_from
        # Дата поступления на склад
        el.add_date = add_date
        return el

    @staticmethod
    def get_copier_count(self):
        return self.count
