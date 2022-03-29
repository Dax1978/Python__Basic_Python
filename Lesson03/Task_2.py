class TranslateNumber():
    def __init__(self):
        self.engNumber = {
            'Zero': 'Ноль',
            'zero': 'ноль',
            'One': 'Один',
            'one': 'один',
            'Two': 'Два',
            'two': 'два',
            'Three': 'Три',
            'three': 'три',
            'Four': 'Четыре',
            'four': 'четыре',
            'Five': 'Пять',
            'five': 'пять',
            'Six': 'Шесть',
            'six': 'шесть',
            'Seven': 'Семь',
            'seven': 'семь',
            'Eight': 'Восемь',
            'eight': 'восемь',
            'Nine': 'Девять',
            'nine': 'девять',
            'Ten': 'Десять',
            'ten': 'десять',
        }
        self.num_translate()

    # Метод для перевода
    def num_translate(self):
        # Бесконечный цикл, с выходом по вводу 'quit' или 'Quit'
        while True:
            num = input('Введите название цифры от 0 до 10 на английском, с большой или малой буквы\n'
                        '(Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine, Ten)\n'
                        'Для выхода наберите quit или Quit: ')
            # Обработка команд на выход из бесконечного цикла
            if num == 'quit' or num == 'Quit': break
            # Проверка наличия такого ключа.
                # Если есть -> переводим
                # Если нет такого -> None
            if num in self.engNumber: print(self.engNumber[num])
            else: print('None\n')

if __name__ == '__main__':
    tn = TranslateNumber()