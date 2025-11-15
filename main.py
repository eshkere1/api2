import requests


API_KEY="d1e2691a52f3894b1076886c"


def get_conversion_rates(currency):
    url=f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/RUB"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()["conversion_rates"]


def get_target_money(base_money, target_currency, conversion_rates):
    factor = conversion_rates[target_currency.upper()]
    return int(base_money) * factor


if __name__ == "__main__":
    base_currency = input("Введите код базовой валюты(например rub):")
    target_currency = input("Введите код целевой валюты(например rub):")
    base_money = input("Введите сумму")
    print(get_target_money(base_money, target_currency, get_conversion_rates(base_currency)))
