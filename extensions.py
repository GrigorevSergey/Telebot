import requests
import json
from config import currency


class APIException(Exception):
    pass

class CurrencyConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        if quote == base:
            raise APIException(f'Невозможно конвертировать одинаковые параметры {base}')

        try:
            quote_currency = currency[quote]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {quote}')

        try:
            base_currency = currency[base]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {base}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_currency}&tsyms={base_currency}')
        total_base = json.loads(r.content)[currency[base]] * int(amount)

        return total_base