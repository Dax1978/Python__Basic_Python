####################################################################################################################
#                                                                                                                  #
# Задача 1                                                                                                         #
#                                                                                                                  #
####################################################################################################################

class MyDate():
    __date = ''

    def __init__(self, dt) -> None:
        MyDate.__date = dt

    @classmethod
    def getDate(cls):
        cls.__date = tuple(map(lambda x: int(x), cls.__date.split('-')))
        print(cls.__date)
        print("Дата: ", cls.__date[0], " Тип данных: ", type(cls.__date[0]))
        print("Месяц: ", cls.__date[1], " Тип данных: ", type(cls.__date[1]))
        print("Год: ", cls.__date[2], " Тип данных: ", type(cls.__date[2]))

    @staticmethod
    def trueDate(dt):
        dt = dt.split('-')
        # Проверка на корректность переданной строки даты
        if len(dt) == 3:
            pass
            # print("Это корректный список!")
        else:
            print("Ошибка! Не кооректная строка даты.")
            print("Дата должна быть в формате 'DD-MM-YYYY'")
            print("Пример: '28-04-2022'")
            return False

        flag = [0, 0, 0]
        # Провека даты
        try:
            dt[0] = int(dt[0])
        except ValueError:
            print("Ошибка! На месте даты не число.")
        except Exception:
            print("Ошибка! Не корректно указана дата")
        else:
            if dt[0] > 0 and dt[0] < 32:
                flag[0] = 1
            else:
                print("Ошибка! Не корректный диапазон указанной даты.")
                return False
        # Провека месяца
        try:
            dt[1] = int(dt[1])
        except ValueError:
            print("Ошибка! На месте месяца не число.")
        except Exception:
            print("Ошибка! Не корректно указан месяц")
        else:
            if dt[1] > 0 and dt[1] < 13:
                flag[1] = 1
            else:
                print("Ошибка! Не корректный диапазон указанного месяца.")
                return False
        # Провека года
        try:
            dt[2] = int(dt[2])
        except ValueError:
            print("Ошибка! На месте года не число.")
        except Exception:
            print("Ошибка! Не корректно указан год")
        else:
            if dt[2] > 0:
                flag[2] = 1
            else:
                print("Ошибка! Год не может быть отрицательный.")
                return False
        return True


MyDate('28-04-2022')
MyDate.getDate()

dt = '28-04-2022'
print(f"Проверка корректности даты '{dt}': ", MyDate.trueDate(dt))
