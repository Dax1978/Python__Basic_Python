
class Tutor_Klass():
    def __init__(self) -> None:
        self.tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей',
                       'Дмитрий', 'Борис', 'Елена', 'Евгений', 'Люба']
        self.klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

    # Метод дополнения количества классов
    def klasses_vs_tutors(self):
        if len(self.tutors) > len(self.klasses):
            for i in range(len(self.tutors) - len(self.klasses)):
                self.klasses.append(None)

    # Генератор кортежей (<tutor>, <klass>)
    def gen_tutor_klass(self):
        for i, tutor in enumerate(self.tutors):
            yield tutor, self.klasses[i]

    # Распечатать значения генератора
    def gen_out(self):
        gen_obj = self.gen_tutor_klass()
        for val in gen_obj:
            print(val)


if __name__ == '__main__':
    task_3 = Tutor_Klass()
    task_3.klasses_vs_tutors()
    task_3.gen_out()
