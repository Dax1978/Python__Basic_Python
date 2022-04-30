import pickle
import datetime

from Task_4_5_6_Printer import Printer
from Task_4_5_6_Scaner import Scaner
from Task_4_5_6_Copier import Copier


class Warehouse():
    def __init__(self) -> None:
        self.warehouse = []
        self.shop = []
        self.readWarehouse()
        self.readShop()

    def viewWarehouse(self):
        for i, el in enumerate(self.warehouse):
            oe = ''
            if type(el).__name__ == "Printer":
                oe = "Принтер"
            if type(el).__name__ == "Scaner":
                oe = "Сканер"
            if type(el).__name__ == "Copier":
                oe = "Ксерокс"
            print(f"Техника №", i + 1, "Тип:", oe)
            print(el)
            print("Поступил:", el.add_date)
            print("Поступил из:", el.add_from)
            print()

    def viewShop(self):
        for el in self.shop:
            if type(el).__name__ == "Printer":
                print("Принтер:")
            if type(el).__name__ == "Scaner":
                print("Сканер:")
            if type(el).__name__ == "Copier":
                print("Ксерокс:")
            print(el)
            print("Поступил на склад:", el.add_date)
            print("Поступил на склад из:", el.add_from)
            print("Выбыл со склада:", el.del_date)
            print("Отправлен в:", el.del_where)
            print()

    def saveWarehouse(self):
        with open('warehouse.db', 'wb') as f:
            pickle.dump(self.warehouse, f)

    def saveShop(self):
        with open('shop.db', 'wb') as f:
            pickle.dump(self.shop, f)

    def readWarehouse(self):
        with open('warehouse.db', 'rb') as f:
            try:
                self.warehouse = pickle.load(f)
            except EOFError:
                print("Еще нет записей в файле.")
            else:
                print(self.warehouse)

    def readShop(self):
        with open('shop.db', 'rb') as f:
            try:
                self.shop = pickle.load(f)
            except EOFError:
                print("Еще нет записей в файле.")
            else:
                print(self.shop)

    def add(self, param):
        if param.lower() == "pa":
            el = Printer.add()
        if param.lower() == "sa":
            el = Scaner.add()
        if param.lower() == "ca":
            el = Copier.add()
        self.warehouse.append(el)
        self.saveWarehouse()

    def send(self):
        min = 1
        max = len(self.warehouse)
        if max < 1:
            print("На складе нет запаса оргтехники.")
        else:
            num = Printer.int_value(
                "Укажите номер перемещаемой позиции со склада: ", min, max)
            del_where = input("Укажите место назначения: ")
            del_date = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
            el = self.warehouse.pop(num - 1)
            el.del_where = del_where
            el.del_date = del_date
            self.shop.append(el)
            self.saveWarehouse()
            self.saveShop()
