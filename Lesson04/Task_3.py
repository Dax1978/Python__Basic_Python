import requests
import xml.etree.ElementTree as ET

# Для работы с Decimal необходимо подключить данный модуль
from decimal import Decimal
import decimal

# Для парсинга XML был подсмотрен код:
# https://stackoverflow.com/questions/18308529/python-requests-package-handling-xml-response


class Currency_rate():          # Класс для получения текущего курса валют
    # В конструкторе считываем URL из API центробанка
    def __init__(self):
        self.url = "http://www.cbr.ru/scripts/XML_daily.asp"
        self.current_date = ''
        self.exchange = {}
        self.root = ''

        self.get_XML()
        self.current_date_from_request()
        self.current_rate_to_dict_decimal()

    # Метод получения данных XML из запроса requests
    def get_XML(self):
        response = requests.get(self.url)
        self.root = ET.fromstring(response.content)

    # Метод получения даты запроса
    # В данном случае для даты используется тип данных String
    def current_date_from_request(self):
        self.current_date = self.root.attrib['Date']

    # Метод для перевода XML в словарь Обозначение_валюты: float_текущей_ставки
    def current_rate_to_dict_float(self):
        for child in self.root:
            self.exchange[child[1].text] = float(
                child[4].text.replace(',', '.'))

    # Метод для перевода XML в словарь Обозначение_валюты: decimal_текущей_ставки
    # Не сильно усложнилось
    def current_rate_to_dict_decimal(self):
        for child in self.root:
            self.exchange[child[1].text] = Decimal(
                child[4].text.replace(',', '.'))

    # Вывод значения текущего курса
    # Вот только точность Decimal, что то не срабатывает
    def currency_rates(self, currency, precision=4):
        decimal.getcontext().prec = precision
        if currency.upper() in self.exchange:
            return Decimal(self.exchange[currency.upper()])
        else:
            return 'None'


if __name__ == "__main__":
    curr_rate = Currency_rate()
    print('Дата запроса данных: ', curr_rate.current_date)
    print('Курс доллара "USD": ', curr_rate.currency_rates('USD', 5), ' руб.')
    print('Курс доллара "usd": ', curr_rate.currency_rates('usd'), ' руб.')
    print('Курс евро "EUR": ', curr_rate.currency_rates('EUR'), ' руб.')
    print('Курс евро "eur": ', curr_rate.currency_rates('eur'), ' руб.')
    print('Курс неизвестной валюты "ППП": ',
          curr_rate.currency_rates('ППП'))
    print('Тип значения курса на примере "eur": ',
          type(curr_rate.currency_rates('eur')))
