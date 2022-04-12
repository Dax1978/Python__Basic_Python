'''
Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов
web-сервера nginx_logs.txt
*(вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла
логов из предыдущего задания.
Примечание: спамер — это клиент, отправивший больше всех запросов; код должен работать
даже с файлами, размер которых превышает объем ОЗУ компьютера.
'''


class Parsing_Web_log():                                            # Класс для работы по разбору лога
    def __init__(self, filename) -> None:
        # Свойство, для хранения имени файла, с которым будем работать
        self.filename = filename
        # Свойство, для хранения файловой переменной
        self.file = self.open_file()
        # Свойство, хранящее генератор для чтения строк из файла
        self.generator = self.create_generator()
        # Свойство, где будет сохраняться список согласно задания №1
        self.list_log = []
        # Свойство, где сохраняется список всех записанных в логе адресов
        self.addr_log = []

    # Метод для открытия файла на чтение. Возвращает открытый файл
    def open_file(self):
        return open(self.filename, 'r', encoding='utf-8')

    # Метод, возвращающий генератор чтения данных из файла
    def create_generator(self):
        return (line for line in self.file)

    # Метод, возвращающий кортеж из прочтенной строки, полученной из генератора
    def create_tuple_from_web_string(self):
        line = next(self.generator).split(" ")
        return line[0], line[5][1:], line[6]

    # Метод, заполняющий спики: список кортежей согласно задания №1, и список адресов
    def create_list_log(self):
        for line in self.generator:
            curr_line = self.create_tuple_from_web_string()
            self.list_log.append(curr_line)
            self.addr_log.append(curr_line[0])

    # Метод, для определения количества обращений с каждого адреса. возвращает адрес,
    # с которого производилось максимальное число обращений и количество обращений
    def search_spamer(self):
        request_count = 0
        request_addr = ''
        for item in list(set(self.addr_log)):
            if self.addr_log.count(item) > request_count:
                request_count = self.addr_log.count(item)
                request_addr = item
        return request_addr, request_count

    # Метод, возвращающий лог, согласно задания №1
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
    log.create_list_log()
    # Выводим список лога, согласно задания №1
    print('Выводим наш список кортежей вида (<remote_addr>, <request_type>, <requested_resource>):')
    print(log.get_log())
    # Ищем спамера и сохраняем в переменной spamer
    spamer = log.search_spamer()
    # Показываем нашего спамера
    print(f'Пользователь с адреса {spamer[0]} обращался {spamer[1]} раз!')
    print('Высока вероятность, что это спамер!')
