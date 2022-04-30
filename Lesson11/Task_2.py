####################################################################################################################
#                                                                                                                  #
# Задача 2                                                                                                         #
#                                                                                                                  #
####################################################################################################################

class MyErronZeroDivision(Exception):
    def __init__(self, txt='') -> None:
        if len(txt) > 0:
            self.message = txt
        else:
            self.message = "Ошибка! Вызвано исключение MyErronZeroDivision"

    def __str__(self):
        if self.message:
            return "MyErronZeroDivision: {0} ".format(self.message)
        else:
            return "MyErronZeroDivision has been raised"


try:
    num = float(input("Введите знаменатель дроби '77 / x': x = "))
    if num == 0:
        raise MyErronZeroDivision("Ай-яй-яй! Попытка деления на ноль")
except ValueError:
    print("Вы ввели не число")
except MyErronZeroDivision as err:
    print(err)
else:
    print("77 /", num, "=", 77 / num)
