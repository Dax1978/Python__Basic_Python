class Odd_Numbers():
    def __init__(self, max_num) -> None:
        self.max_num = max_num

    # Задача 1
    # Написать генератор нечётных чисел от 1 до n (включительно),
    # используя ключевое слово yield
    def generator_odd_number_yield(self):
        for num in range(1, self.max_num + 1, 2):
            yield num

    # Задача 2 *(вместо 1)
    #  Решить задачу генерации нечётных чисел от 1 до n (включительно),
    # не используя ключевое слово yield
    def generator_odd_number(self):
        return (num for num in range(1, self.max_num + 1, 2))

    # Распечатать значения генератора от 1 до max_num включительно
    def gen_out(self):
        gen_obj = self.generator_odd_number()
        for val in gen_obj:
            print(val)


if __name__ == '__main__':
    my_gen = Odd_Numbers(7)
    # task_1_gen = my_gen.generator_odd_number_yield(7)
    # print('Текущее значение: ', next(task_1_gen))
    # print('Текущее значение: ', next(task_1_gen))
    # print('Текущее значение: ', next(task_1_gen))
    # print('Текущее значение: ', next(task_1_gen))
    # print('Текущее значение: ', next(task_1_gen))
    # task_2_gen = my_gen.generator_odd_number()
    # print('Текущее значение: ', next(task_2_gen))
    # print('Текущее значение: ', next(task_2_gen))
    # print('Текущее значение: ', next(task_2_gen))
    # print('Текущее значение: ', next(task_2_gen))
    # print('Текущее значение: ', next(task_2_gen))
    task_2_gen_all = my_gen.gen_out()
