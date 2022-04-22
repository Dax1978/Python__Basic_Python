####################################################################################################################
# Задание 1                                                                                                        #
# Создать класс TrafficLight (светофор)                                                                            #
# -  определить у него один атрибут color (цвет) и метод running (запуск);                                         #
# - атрибут реализовать как приватный;                                                                             #
# - в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;                         #
# - продолжительность первого состояния (красный) составляет 7 секунд,                                             #
#        второго (жёлтый) — 2 секунды,                                                                             #
#        третьего (зелёный) — на ваше усмотрение;                                                                  #
# - переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);       #
# - проверить работу примера, создав экземпляр и вызвав описанный метод.                                           #
####################################################################################################################

import time


class TrafficLight():
    def __init__(self) -> None:
        self.__color = 'красный'

    def __change_color(self):
        if self.__color == 'красный':
            time.sleep(7)
            self.__color = 'желтый'
        elif self.__color == 'желтый':
            time.sleep(2)
            self.__color = 'зеленый'
        else:
            time.sleep(5)
            self.__color = 'красный'

    def running(self):
        try:
            print('Для выхода нажмитие Ctrl+C')
            while True:
                print('Сигнал светофора: ', self.__color)
                self.__change_color()
        except:
            print('Завершение программы...')


trafficLight = TrafficLight()
trafficLight.running()
