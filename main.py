import requests
import os
import argparse
from dotenv import load_dotenv


def get_conversion_rates(currency, api_key):
    url=f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{currency.upper()}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()["conversion_rates"]


def get_target_money(base_money, target_currency, conversion_rates):
    curse = conversion_rates[target_currency.upper()]
    print(f"Курс: {curse}")
    return float(base_money) * curse


def main():
    load_dotenv()
    api_key=os.getenv("API_KEY")
    parser = argparse.ArgumentParser(description=" Эта программа переводит деньги на другую валюту")
    parser.add_argument("-b", "--base", help="Введите код базовой валюты(например rub)", required=True)
    parser.add_argument("-t", "--target", help="Введите код целевой валюты(например eur)", required=True)
    parser.add_argument("-a", "--amount", help="Введите сумму", required=True)
    args = parser.parse_args()
    try:
        print(f"Конвертируемая сумма: {get_target_money(args.amount, args.target, get_conversion_rates(args.base, api_key))} {args.target.upper()}")
    except HTTPError:
        print("Вы допустили ошибку в запросе")
    

if __name__ == "__main__":
    main()
    
