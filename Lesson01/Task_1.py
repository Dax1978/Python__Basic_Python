# Реализовать вывод информации о промежутке времени
# в зависимости от его продолжительности duration
# в секундах: до минуты: < s > сек;
# в минутах до часа: < m > мин < s > сек;
# в часах до суток: < h > час < m > мин < s > сек;
# в остальных случаях: < d > дн < h > час < m > мин < s > сек.

class Time2human():
    def __init__(self, t):
        self.t = t
        self.res = ''

    def humanTime(self):
        self.t = self.tDay()
        self.t = self.tHour()
        self.t = self.tMinunte()
        self.t = self.tSecond()

        print(self.res)

    def tDay(self):
        if self.t >= 86400:
            self.res = str(self.t // 86400) + ' дн. '
            return self.t % 86400
        else:
            return self.t

    def tHour(self):
        if self.t >= 3600:
            self.res += str(self.t // 3600) + ' час. '
            return self.t % 3600
        else:
            return self.t

    def tMinunte(self):
        if self.t >= 60:
            self.res += str(self.t // 60) + ' мин. '
            return self.t % 60
        else:
            return self.t

    def tSecond(self):
        self.res += str(self.t) + ' сек. '


if __name__ == '__main__':
    try:
        duration = int(input('Укажите значение интересующей эпохи в виде целого числа: '))
    except ValueError:
        print("Попробуйте в следующий раз все таки найти на клавиатуре цифры и набрать именно целое число!")
    else:
        htime = Time2human(duration)
        htime.humanTime()