###################################################################################################################################
# Задание 2                                                                                                                       #
# Написать регулярное выражение для парсинга файла логов web-сервера из ДЗ 6 урока nginx_logs.txt  для получения информации вида: #
# (<remote_addr>, <request_datetime>, <request_type>, <requested_resource>, <response_code>, <response_size>)                     #
###################################################################################################################################

import re


class Parsing_Web_log():                                            # Класс для работы по разбору лога
    def __init__(self, filename) -> None:
        # Свойство, для хранения имени файла, с которым будем работать
        self.filename = filename
        # Свойство, для хранения файловой переменной
        self.file = self.open_file()
        # Свойство, хранящее генератор для чтения строк из файла
        self.generator = self.create_generator()
        # Свойство, где будет сохраняться список согласно задания
        self.list_log = []

    # Метод для открытия файла на чтение. Возвращает открытый файл
    def open_file(self):
        return open(self.filename, 'r', encoding='utf-8')

    # Метод, возвращающий генератор чтения данных из файла
    def create_generator(self):
        return (line for line in self.file)

    # Метод, возвращающий кортеж из прочтенной строки, полученной из генератора
    def create_tuple_from_web_string(self):
        for line in self.generator:
            tup = []
            remote_addr = re.search(
                r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|[a-z0-9]{1,4}:[a-z0-9]{1,4}:[a-z0-9]{1,4}:[a-z0-9]{1,4}:[a-z0-9]{1,4}:[a-z0-9]{1,4}:[a-z0-9]{1,4}:[a-z0-9]{1,4}|[a-z0-9]{4}:[a-z0-9]{4}::[a-z0-9]{4}:[a-z0-9]{4}:[a-z0-9]{4}:[a-z0-9]{4}|[a-z0-9]{1,4}:[a-z0-9]{1,4}:[a-z0-9]{1,4}:[a-z0-9]{1,4}::\d+', line)
            request_datetime = re.search(
                '\d{2}/\w{3}/\d{4}:\d{2}:\d{2}:\d{2}\s\+\d{4}', line)
            request_type = re.search('GET|HEAD', line)
            requested_resource = re.search(
                '(?<= )/[A-Za-z/_0-9.\sHTTP]+', line)
            response_code = re.search(
                '(?<=" )\d+', line)
            response_size = re.search(
                '\d+(?= "-")|\d+(?= "http)', line)
            tup = remote_addr.group(0), request_datetime.group(0), request_type.group(
                0), requested_resource.group(0), response_code.group(0), response_size.group(0)
            print('raw = ', line.split('\n'))
            print('parsed_raw = ', tup)
            # self.list_log.append(tup)

    # Метод, возвращающий лог, согласно задания №2
    def get_log(self):
        return(self.list_log)

    # Деструктор, в котором закрываем файл, т.к. мы больше не работаем с ним
    def __del__(self):
        self.file.close()
        print("Файл закрыт...")


if __name__ == '__main__':
    # Создаем объект log
    log = Parsing_Web_log('nginx_logs.txt')
    # Создаем списки логов из файла
    log.create_tuple_from_web_string()
    # Выводим список лога, согласно задания №2
    # print('Выводим наш список кортежей вида (<remote_addr>, <request_datetime>, <request_type>, <requested_resource>, <response_code>, <response_size>):')
    # print(log.get_log())
