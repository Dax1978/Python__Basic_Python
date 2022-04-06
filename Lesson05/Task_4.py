class More_previous():
    def __init__(self) -> None:
        self.src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
        self.result = []

    # Генератор для прохода по значениям заданного списка
    def gen_list(self):
        return (num for num in self.src)

    # Заполняем список self.result значениями,
    # которые больше предыдущих значений
    def list_more_previous(self):
        gen_obj = self.gen_list()
        value_previous = next(gen_obj)
        for value_current in gen_obj:
            if value_current > value_previous:
                self.result.append(value_current)
            value_previous = value_current


if __name__ == '__main__':
    task_4 = More_previous()
    task_4.list_more_previous()
    print('result = ', task_4.result)
