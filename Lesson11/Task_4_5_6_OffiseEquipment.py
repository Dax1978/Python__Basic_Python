class OfficeEquipment():
    def __init__(self, brend, model) -> None:
        self.brend = brend
        self.model = model
        self.add_date = ''
        self.add_from = ''
        self.del_date = ''
        self.del_where = ''

    def __str__(self) -> str:
        str = f"Производитель: {self.brend}\n"
        str += f"Модель: {self.model}\n"
        return str

    # Общий метод Контроля ввода целого числа в установленном диапазоне
    @classmethod
    def int_value(cls, msg, min, max):
        while True:
            value = input(msg)
            try:
                value = int(value)
            except:
                print("Вы ввели некорректное значение.")
                print("Программа ожидает ввода целого числа.")
            else:
                if value >= min and value <= max:
                    return value
                print("Ваше значение вне допустимого диапазона.")
