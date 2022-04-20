####################################################################################################################
# Задание 1                                                                                                        #
# Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает имя            #
# пользователя и почтовый домен из email адреса и возвращает их в виде словаря. Если адрес не валиден, выбросить   #
# исключение ValueError.                                                                                           #
####################################################################################################################

import re


class ValueError(Exception):
    pass


def email_parse(email):
    username = re.search(r'^[a-zA-Z0-9_.+-]+', email)
    domain = re.search(r'(?<=@)[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email)
    if username:
        if domain:
            return dict(username=username.group(0), domain=domain.group(0))
        else:
            raise ValueError(
                "Не верно указан почтовый домен в адресе: " + email)
        # return dict(username=username.group(0), domain=domain.group(0)) if domain else "Не верно указан почтовый домен"
    # return "Не верно указано имя пользователя"
    raise ValueError("Не верное имя пользователя: " + email)


if __name__ == "__main__":
    print(email_parse('Someone@geekbrains.ru'))
    print(email_parse('Some-one@geekbrains.ru'))
    print(email_parse('Some_one@geekbrains.ru'))
    # print(email_parse('%%Someone@geekbrains.ru'))
    print(email_parse('Someone@geekbrainsru'))
