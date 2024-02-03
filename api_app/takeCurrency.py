import requests
import json
import datetime
from .models import Currency, ExchangeRate

TOKEN = 'f3d9564f09be38ea0ac2b70b'

def takeCurrency(currency):
    url = f'https://v6.exchangerate-api.com/v6/{TOKEN}/latest/{currency}'
    headers = {'Aunthentication': f'Bearer {TOKEN}'}
    response = requests.get(url, headers=headers)
    data = response.json()
    base_currency = data['base_code']

    # example: "time_next_update_utc": "Fri, 02 Feb 2024 00:00:01 +0000",
    time_last_update = datetime.datetime.strptime(data['time_last_update_utc'], "%a, %d %b %Y %H:%M:%S %z")
    time_next_update = datetime.datetime.strptime(data['time_next_update_utc'], "%a, %d %b %Y %H:%M:%S %z")

    rates = data['conversion_rates']

    for currency in rates:
        currency_base = Currency.objects.get_or_create(name=base_currency)[0]
        currency_final = Currency.objects.get_or_create(name=currency)[0]
        rate = rates[currency]
        ExchangeRate.objects.get_or_create(currency_base=currency_base, currency_final=currency_final, time_last_update=time_last_update, time_next_update=time_next_update , rate=rate)
    return 'Data updated'