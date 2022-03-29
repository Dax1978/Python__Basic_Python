
class EndingWord():
    def __init__(self):
        self.percentes()

    def ending(self, value):
        if (int(str(value)[-2:])) > 10 and (int(str(value)[-2:])) < 20:
            return ' процентов'
        elif int(str(value)[-1]) == 1:
            return ' процент'
        elif int(str(value)[-1]) > 1 and int(str(value)[-1]) < 5:
            return ' процента'
        elif (int(str(value)[-1]) >= 5 and int(str(value)[-1]) < 10) or int(str(value)[-1]) == 0:
            return ' процентов'

    def percentes(self):
        for i in range(1, 101):
            print(str(i) + self.ending(i))

if __name__ == '__main__':
    p = EndingWord()