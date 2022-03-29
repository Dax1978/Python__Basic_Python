import random

class Greeting:
    def __init__(self):
        # Исходный заданный список
        self.initialList = ['инженер-конструктор Игорь',
                       'главный бухгалтер МАРИНА',
                       'токарь высшего разряда нИКОЛАй',
                       'директор аэлита']
        # Приветствие. Список для разнообразия
        self.addition = ['Добрый день, ',
                    'Привет, ',
                    'Здравствуйте, ',
                    'Доброе утро, ',
                    'Добрый вечер, ']
        # Работаем сразу при инициации
        self.nameGreeting()

    # Здесь все и происходит
    def nameGreeting(self):
        for elem in self.initialList:
            print(random.choice(self.addition) + elem.split()[-1].capitalize() + '!')

if __name__ == '__main__':
    gr = Greeting()