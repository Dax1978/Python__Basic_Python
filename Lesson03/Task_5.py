import random

'''
Класс для генерации шуток из 3 слов: существительное + глагол + прилагательное
Слова выбираются из заранее созданных списков из 5 слов
В объект в качестве параметра передается количество шуток как целое число
и необязательный флаг True/False для разрешения или запрещения повторения слов в шутках.
По умолчанию повторение слов в шутках запрещено.
Если повторение запрещено, то количество шуток не может быть больше 5.
Если повторение разрешено, то количество шуток неограничено. 
'''
class Jokes():
    def __init__(self, num, repeat = False):
        self.nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
        self.adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
        self.adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
        self.num = num
        self.repeat = repeat
        self.listNouns = []
        self.listAdverbs = []
        self.listAdjectives = []

        self.get_jokes(self.num)

    # Метод (Функция) генерации шуток
    '''
    1. Проверяем флаг возможности повторения слов в шутках.
    2. Если повторение запрещено и шуток просят больше 5 - Предупреждаем!
    3. Иначе генерируем шутки, столько сколько просят.
       При этом слова выбираются из списков в отдельных методах, в которых учитывается флаг
       можно ли повторять слова или нет.
    '''
    def get_jokes(self, num):
        if not self.repeat and num > 5:
            print('Нельзя указать количество больше 5, если повторение запрещено...')
        else:
            for i in range(num):
                strJoke = ''
                strJoke += self.get_nonus() + ' ' + self.get_adverbs() + ' ' + self.get_adjectives()
                print(strJoke)

    # Генератор случайного выбора существительного
    def get_nonus(self):
        if self.repeat:
            str = random.choice(self.nouns)
        else:
            while True:
                str = random.choice(self.nouns)
                if not str in self.listNouns: break
        self.listNouns.append(str)
        return str

    # Генератор случайного выбора глагола
    def get_adverbs(self):
        if self.repeat:
            str = random.choice(self.adverbs)
        else:
            while True:
                str = random.choice(self.adverbs)
                if not str in self.listAdverbs: break
        self.listAdverbs.append(str)
        return str

    # Генератор случайного выбора прилагательного
    def get_adjectives(self):
        if self.repeat:
            str = random.choice(self.adjectives)
        else:
            while True:
                str = random.choice(self.adjectives)
                if not str in self.listAdjectives: break
        self.listAdjectives.append(str)
        return str


if __name__ == '__main__':
    # Иницируем объект с условием вывода 5 шуток, с запретом на повторение по умолчанию
    jk_1 = Jokes(5)
    # Иницируем объект с условием вывода 7 шуток, с запретом на повторение
    jk_2 = Jokes(7, False)
    # Иницируем объект с условием вывода 7 шуток, с разрешением на повторение
    jk_3 = Jokes(7, True)