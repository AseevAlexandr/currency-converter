import requests

API_KEY = '32e42d5c6f7d0b695b100063e7d5f261'
API_URL = f"http://api.coinlayer.com/live?access_key={API_KEY}"


def get_exchange_rates():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        return None


# print(get_exchange_rates())