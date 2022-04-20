###################################################################################################################################
# Задание 3                                                                                                                       #
# Написать декоратор для логирования типов позиционных аргументов функции                                                         #
###################################################################################################################################
def type_logger(func):
    def wrapper(*args, **kwargs):
        print('Аргумент: ' + str(args[0]) + ' Тип: ' + str(type(args[0])))
        # print("Это сообщение будет напечатано до вызова функции.")
        val = func(*args, **kwargs)
        print('Результат: ' + str(val) + ' Тип: ' + str(type(val)))
        # print("Это сообщение будет напечатано после вызова функции.")
        return val
    return wrapper


def type_logger_nums(func):
    def wrapper(*args, **kwargs):
        res = ''
        for num in args:
            res += 'Аргумент: ' + str(num) + ' Тип: ' + str(type(num)) + ', '
        print(res[:-2])
        val = func(*args, **kwargs)
        print('Результат: ' + str(val) + ' Тип: ' + str(type(val)))
        return val
    return wrapper


def type_logger_nums_name(func):
    def wrapper(*args, **kwargs):
        res = ''
        for key, value in kwargs.items():
            res += "Аргумент: '{}' : {}".format(key, value) + \
                " Тип: " + str(type(value)) + ', '
        print(res[:-2])
        val = func(*args, **kwargs)
        print('Результат: ' + str(val) + ' Тип: ' + str(type(val)))
        print('Декоратор вызван для функции: ', func.__name__)
        return val
    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


@type_logger_nums
def calc_cube_sum_nums(*nums):
    sum = 0
    for n in nums:
        sum += n
    return sum ** 3


@type_logger_nums_name
def calc_cube_sum_nums_name(**kwargs):
    sum = 0
    for key, value in kwargs.items():
        sum += value
    return sum ** 3


print('Тест декоратора для функции с одной переменной:')
calc_cube(5)
print('\nТест декоратора для функции с различным числом переменных:')
calc_cube_sum_nums(5)
print()
calc_cube_sum_nums(1, 2.1, 3)
print('\nТест декоратора для функции с различным числом именнованных переменных:')
calc_cube_sum_nums_name(a=1)
calc_cube_sum_nums_name(a=1, b=2.1)
calc_cube_sum_nums_name(a=1, b=2.1, c=3)
