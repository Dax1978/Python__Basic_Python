#########################################################################################################################
#                                                                                                                       #
# Практическое задание 7                                                                                                #
#                                                                                                                       #
# Задачи 2, 3, 4, 5                                                                                                     #
# В конце листинга расписаны все задачи                                                                                 #
#########################################################################################################################

import os
import sys
import json


class Working_With_System():
    def __init__(self, project="MyProject", templates=False) -> None:
        # Свойство, для хранения наименования проекта
        self.__prj = project
        # Свойство для хранения создаваемой структуры директорий и файлов
        self.__schema_need = []
        # Свойство для хранения пути к текущему каталогу
        self.__curr = os.getcwd().replace("\\", "/")
        # Свойство для хранения результата сосздания структуры
        self.__result_project = ""
        # Свойство для хранения флага вынесения Templates отдельно
        self.__templates = templates
        # Словарь для сохранения статистики по размерам файлов
        self.__dict_size = {
            100: 0,
            1000: 0,
            10000: 0,
            100000: 0,
            1000000: 0,
            10000000: 0,
            100000000: 0
        }
        # Словарь для сохранения более полной статистики по размерам файлов
        self.__dict_size_full = {
            100: [0, set()],
            1000: [0, set()],
            10000: [0, set()],
            100000: [0, set()],
            1000000: [0, set()],
            10000000: [0, set()],
            100000000: [0, set()]
        }
        # Итоговый словарь для сохранения в json
        self.__dict_size_full_loc = {}
        # Свойство для хранения наименования json файла
        self.__json_dict = ''

        # Чтение файла конфигурации
        self.__result_config = self.__config('config.yaml')
        # Если результат чтения файла конфигурации True запускаем метод создания структуры проекта
        if self.__result_config:
            self.__result_project = self.__create_project()
            print('Создание структуры проекта "' + self.__prj + '" завершено!') if self.__result_project else print(
                'Ошибка создания структуры проекта "' + self.__prj + '"...')
        else:
            print('Отсутствует файл конфигурации "config.yaml"...')

    # Метод проверки наличия директории
    # Возвращает True если такая директория уже существует
    # Возвращает False если такой директории нет по указанному пути (Путь свободен!)
    def __dir(self, name):
        return True if os.path.isdir('./' + name) else False
        # os.path.exists('./dir') можно и так проверить

    # Метод проверки наличия файла
    # Возвращает True если такой файл уже существует
    # Возвращает False если такого файла нет по указанному пути
    def __file(self, name):
        return True if os.path.isfile('./' + name) else False
        # os.path.exists('./dir') можно и так проверить

    # Чтение файла конфигурации config.yaml
    def __config(self, name):
        # Проверяем наличие такого файла
        # Если файл существует, пробуем читать
        if self.__file(name):
            # Ловим исключения при чтении файла
            try:
                with open(name, "r") as f:
                    for line in f:
                        # Записываем в список self.__schema_need списки, сформированные из файла конфигурации
                        self.__schema_need.append(
                            line.strip().lstrip('/').rstrip('/').split('/'))

            except Exception:
                # Если пошли ошибки, выводим сообщение и возвращаем значение метода False
                print('Возникли ошибки при чтении файла конфигурации "config.yaml"')
                return False
            else:
                # Если все прошло хорошо, возвращаем значение True
                return True
        else:
            # Если файла конфигурации нет, то возвращаем значение метода False
            return False

    # Создаем пустой проект
    def __create_project(self):
        # Проверяем в начале, может такой проект уже существует
        if self.__dir(self.__prj):
            # Если такой проект уже есть, сообщаем об этом, выходим и возвращаем False
            print('Проект "' + self.__prj + '" уже существует!')
            return False
        else:
            # Если такого проекта нет:
            # Создаем локальную переменную, где будем хранить длину строки с путем до templates в стандартном варианте
            len_templates = 0
            # Создаем директорию под проект
            os.mkdir(self.__curr + '/' + self.__prj)

            # Если флаг templates у нас True, то создаем в директории проекта директорию "templates", куда и будем сохранять все templates
            if self.__templates:
                os.mkdir(self.__curr + '/' + self.__prj + '/templates')

            # Проходим по списку списков self.__schema_need
            for elem_0 in self.__schema_need:
                # В локальной переменной new_path путь к проекту
                new_path = self.__curr + '/' + self.__prj
                # Переходим в директорию с проектом
                os.chdir(new_path)
                # Проходим по всем элементам списка, каждого элемента списка self.__schema_need
                # И формируем путь итоговый путь
                for elem_1 in elem_0:
                    new_path += '/' + elem_1

                # Если флаг templates у нас True, то
                if self.__templates:
                    # Если последний элемент был 'templates', запоминаем длину этой строки и пропускаем этот цикл
                    if new_path[-9:] == 'templates':
                        len_templates = len(new_path)
                        continue
                    # Если 'templates' есть в пути, но он не последний, то заменяем первую часть пути на путь до созданной директории 'templates' в корне проекта
                    if ('templates' in new_path and new_path[-9:] != 'templates'):
                        new_path = self.__curr + '/' + self.__prj + \
                            '/templates' + new_path[len_templates:]

                # Проверяем, если это путь к файлу, то создаем файл
                if ('.' in new_path):
                    open(new_path, 'w')
                # Иначе, это директория, тогда создаем директорию и переходим в нее
                else:
                    os.mkdir(new_path)
                    os.chdir(new_path)
            # Возвращаемся в корневую директорию из проекта
            os.chdir("..")
            return True

    # Статистика директории
    def statistic(self, path):
        if os.path.isdir(path):
            for elem in os.listdir(path):
                elem = path + '/' + elem
                if os.path.isfile(elem):
                    if os.stat(elem).st_size <= 100:
                        self.__dict_size[100] += 1
                    elif os.stat(elem).st_size > 100 and os.stat(elem).st_size <= 1000:
                        self.__dict_size[1000] += 1
                    elif os.stat(elem).st_size > 1000 and os.stat(elem).st_size <= 10000:
                        self.__dict_size[10000] += 1
                    elif os.stat(elem).st_size > 10000 and os.stat(elem).st_size <= 100000:
                        self.__dict_size[100000] += 1
                    elif os.stat(elem).st_size > 100000 and os.stat(elem).st_size <= 1000000:
                        self.__dict_size[1000000] += 1
                    elif os.stat(elem).st_size > 1000000 and os.stat(elem).st_size <= 10000000:
                        self.__dict_size[10000000] += 1
                    elif os.stat(elem).st_size > 10000000:
                        self.__dict_size[100000000] += 1
                if os.path.isdir(elem):
                    os.chdir(elem)
                    self.statistic(elem)
            os.chdir('..')
        else:
            print("Указанной Вами директории " + path + " не существует.")

    # Распечатываем статистику
    def print_statistic(self):
        print(self.__dict_size)

    # Более полная статистика директории
    def statistic_full(self, path):
        if os.path.isdir(path):
            for elem in os.listdir(path):
                elem = path + '/' + elem
                if os.path.isfile(elem):
                    if os.stat(elem).st_size <= 100:
                        self.__dict_size_full[100][0] += 1
                        self.__dict_size_full[100][1].add(
                            os.path.splitext(elem)[1])
                    elif os.stat(elem).st_size > 100 and os.stat(elem).st_size <= 1000:
                        self.__dict_size_full[1000][0] += 1
                        self.__dict_size_full[1000][1].add(
                            os.path.splitext(elem)[1])
                    elif os.stat(elem).st_size > 1000 and os.stat(elem).st_size <= 10000:
                        self.__dict_size_full[10000][0] += 1
                        self.__dict_size_full[10000][1].add(
                            os.path.splitext(elem)[1])
                    elif os.stat(elem).st_size > 10000 and os.stat(elem).st_size <= 100000:
                        self.__dict_size_full[100000][0] += 1
                        self.__dict_size_full[100000][1].add(
                            os.path.splitext(elem)[1])
                    elif os.stat(elem).st_size > 100000 and os.stat(elem).st_size <= 1000000:
                        self.__dict_size_full[1000000][0] += 1
                        self.__dict_size_full[1000000][1].add(
                            os.path.splitext(elem)[1])
                    elif os.stat(elem).st_size > 1000000 and os.stat(elem).st_size <= 10000000:
                        self.__dict_size_full[10000000][0] += 1
                        self.__dict_size_full[10000000][1].add(
                            os.path.splitext(elem)[1])
                    elif os.stat(elem).st_size > 10000000:
                        self.__dict_size_full[100000000][0] += 1
                        self.__dict_size_full[100000000][1].add(
                            os.path.splitext(elem)[1])
                if os.path.isdir(elem):
                    os.chdir(elem)
                    self.statistic_full(elem)
            self.__json_dict = os.getcwd().replace("\\", "/").split('/')[-1]
            os.chdir('..')
        else:
            print("Указанной Вами директории " + path + " не существует.")

    # Распечатываем расширенную статистику
    def print_statistic_full(self):
        # Сохраняем полученный словарь self.__dict_size_full в необходимый нам формат в словарь self.__dict_size_full_loc
        for key in self.__dict_size_full.keys():
            self.__dict_size_full_loc[key] = (
                self.__dict_size_full[key][0], list(self.__dict_size_full[key][1]))
        # Конвертируем полученный словарь в json
        json_dict = json.dumps(self.__dict_size_full_loc)
        # Создаем имя файла, как задано
        self.__json_dict += '_summary.json'
        # Сохраняем в файл, в формате json
        with open(self.__json_dict, "w") as f:
            f.write(json_dict)
        # Распечатываем полученный словарь
        print(self.__dict_size_full_loc)


if __name__ == "__main__":
    # Создаем переменные:
    # Templates по умолчанию стандартно, как в задаче 2
    # Наименование проекта по умолчанию "MyProject"
    templates = False
    name_prj = "MyProject"

    # Если есть аргументы командной строки:
    if len(sys.argv) > 1:
        # Если 2-ой аргумент не '-t', то принимаем его как наименование проекта
        if sys.argv[1] != '-t':
            name_prj = sys.argv[1]
        # Проходим по всем аргументам и смотрим
        # Если есть аргумент -t, то указываем, что пользователь хочет создать templates в отдельной директории
        for param in sys.argv:
            if param == '-t':
                templates = True

    # wws = Working_With_System(name_prj, templates)

    #########################################################################################################################
    #                                                                                                                       #
    # Задача 2 (вместо задачи 1)                                                                                            #
    #                                                                                                                       #
    # Создаем объект с исходными параметрами: <Наименование проекта>, <Параметр template = False (по умолчанию False, если  #
    # ничего вторым параметром не указывать)>                                                                               #
    #########################################################################################################################

    task_2 = Working_With_System('Project_Task_2', False)

    #########################################################################################################################
    #                                                                                                                       #
    # Задача 3                                                                                                              #
    #                                                                                                                       #
    # Создаем объект с исходными параметрами: <Наименование проекта>, <Параметр template = False (по умолчанию False, если  #
    # ничего вторым параметром не указывать)>                                                                               #
    # Программно реализована возможность запустить в командной строке с параметрами:                                        #
    #    - указать наименование проекта                                                                                     #
    #    - указать параметр -t. Тогда все шаблоны будут размещены в директории template                                     #
    #########################################################################################################################

    task_3 = Working_With_System('Project_Task_3', True)

    #########################################################################################################################
    #                                                                                                                       #
    # Задача 4                                                                                                              #
    #                                                                                                                       #
    # Выводим статистику по указанной директории, даже если директория содержит вложенные директории. Выводит словарь:      #
    # Ключ - значение байт от предыдущего либо от нуля (для первого диапазона), до ключа включительно (для последнего       #
    # значение верхней границы нет).                                                                                        #
    # Значение - количество файлов в этом диапазоне.                                                                        #
    #########################################################################################################################

    task_4 = Working_With_System('Project_Task_4', False)
    task_4.statistic(
        "D:/Study/Python/0005_Основы_языка_Python_Курс/Lesson07/some_data")
    task_4.print_statistic()

    #########################################################################################################################
    #                                                                                                                       #
    # Задача 5                                                                                                              #
    #                                                                                                                       #
    # Выводим расширенную статистику по указанной директории, даже если директория содержит вложенные директории.           #
    # Выводит словарь: Ключ - значение байт от предыдущего либо от нуля (для первого диапазона), до ключа включительно      #
    # (для последнего значение верхней границы нет).                                                                        #
    # Значение - коретж: количество файлов в этом диапазоне, список с уникальным перчнем типов в этом диапазоне.            #
    #########################################################################################################################

    task_5 = Working_With_System('Project_Task_5', False)
    task_5.statistic_full(
        "D:/Study/Python/0005_Основы_языка_Python_Курс/Lesson07/some_data")
    task_5.print_statistic_full()
