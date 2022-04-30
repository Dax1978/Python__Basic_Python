import datetime
from Task_4_5_6_OffiseEquipment import OfficeEquipment


class Printer(OfficeEquipment):
    count = 0

    def __init__(self, brend, model, paper, matrix_inkjet_laser, black_color) -> None:
        super().__init__(brend, model)
        self.count += 1
        # Количество листов, которые может распечатать
        self.paper = paper
        # 1 - матричный, 2 - струйный, 3 - лазерный
        self.matrix_inkjet_laser = matrix_inkjet_laser
        # 1 - черно-белый, 2 - цветной
        self.black_color = black_color

    def __str__(self) -> str:
        str = super().__str__()
        str += f"Количество распечатываемых листов: {self.paper}\n"
        if self.matrix_inkjet_laser == 1:
            str += f"Тип принтера: матричный\n"
        if self.matrix_inkjet_laser == 2:
            str += f"Тип принтера: струйный\n"
        if self.matrix_inkjet_laser == 3:
            str += f"Тип принтера: лазерный\n"
        if self.black_color == 1:
            str += f"Цветная печать: нет"
        if self.black_color == 2:
            str += f"Цветная печать: да"
        return str

    # Метод добавления Принтера
    @classmethod
    def add(cls):
        brend = input("Укажите бренд принтера: ")
        model = input("Укажите модель принтера: ")
        paper = input(
            "Укажите количество листов, которое может распечатать принтер: ")
        matrix_inkjet_laser = cls.int_value(
            "Укажите 1 или 2 или 3, для матричного, струйного или лазерного принтера соответственно: ", 1, 3)
        black_color = cls.int_value(
            "Укажите 1 или 2, для черно-белого или цветного принтера соответственно: ", 1, 2)
        add_from = input("Укажите откуда прибыл принтер на склад: ")
        add_date = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
        el = Printer(brend, model, paper,
                     matrix_inkjet_laser, black_color)
        # Откуда поступил на склад
        el.add_from = add_from
        # Дата поступления на склад
        el.add_date = add_date
        return el

    @staticmethod
    def get_printer_count(self):
        return self.count
