
class NumFromList:
    def __init__(self, lst):
        self.lst = lst

    # Создаем строку (вместо списка) и выводим ее
    def inStr(self):
        ourStr = ''
        for val in self.lst:
            ourStr += (self.isNumber(val) + ' ')
        print(ourStr)

    # Проверям, что у нас, число или строка?
    def isNumber(self, value):
        if not value[0].isdigit():
            return self.isNumSign(value)
        else:
            return self.isNum(value)

    # Проводим проверку, у нас число?
    # Если да то отдаем его на проверку двузначности, и дополняем двойными ковычками
    # Если нет, то отдаем как есть
    def isNum(self, value):
        if value.isdigit():
            return '"' + self.dblNum(value) + '"'
        else:
            return value

    # Такс, у нас строка, но надо проверить, может первое значение это + или -, а далее число?
    def isNumSign(self, value):
        if (value[0] == '+' or value[0] == '-') and len(value) > 1:
            return '"' + value[0] + self.dblNum(value[1:]) + '"'
        else:
            return value

    # Проверяем на двузначность.
    # Если это однозначное число, то дополняем предстоящим нулем.
    # Если не однозначное, то отдаем как есть
    def dblNum(self, value):
        if len(value) == 1:
            return '0' + value
        else:
            return value


if __name__ == '__main__':
    lst = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
    nfl = NumFromList(lst)
    nfl.inStr()