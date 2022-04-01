import sys
from Task_5_Currency_rate import Currency_rate

if __name__ == "__main__":
    curr_rate = Currency_rate()
    currency = 'USD'
    precision = 4
    if len(sys.argv) == 1:
        currency = 'USD'
    elif len(sys.argv) > 1:
        currency = sys.argv[1].upper()
    elif len(sys.argv) > 2 and sys.argv[2].isdigit():
        precision = int(sys.argv[2])
    # print('Курс валюты "' + currency + '": ' + str(curr_rate.currency_rates(
    #     currency, precision)) + ', ' + curr_rate.current_date)
    print(
        f'Курс валюты "{currency}":  {str(curr_rate.currency_rates(currency, precision))}, {curr_rate.current_date}')
