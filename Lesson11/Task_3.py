####################################################################################################################
#                                                                                                                  #
# Задача 3                                                                                                         #
#                                                                                                                  #
####################################################################################################################

class NotNumber(Exception):
    def __init__(self, msg='') -> None:
        if len(msg) > 0:
            self.message = msg
        else:
            self.message = "Ошибка! Вызвано исключение NotNumber"

    def __str__(self):
        if self.message:
            return "NotNumber: {0} ".format(self.message)
        else:
            return "NotNumber has been raised"


def checkNumber(txt):
    try:
        if not txt.isdigit():
            raise NotNumber("Введено не число")
    except NotNumber as err:
        print(err)
        return False
    else:
        return True


numArr = []
txt = ''
while txt.capitalize() != 'Stop':
    txt = input("Введите число: ")
    if checkNumber(txt):
        numArr.append(int(txt))

print("Сформированный список чисел:")
print(numArr)
