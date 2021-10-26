import requests
import random

API_KEY = "TLO3XsGE9ebJ7QKd4KrWzokPL5GbIXCatPvxAU"
LOCATION_ID = (1, 2 ,3 ,4 ,5 ,6, 7, 8, 9, 10, 11, 12, 13 ,14, 15)

def get_proxy():
    proxy = requests.get(
        f"http://proxy.tinsoftsv.com/api/changeProxy.php?key={API_KEY}&location=0"
    )
    return proxy.json()

def check_ip():
    recent_ip = requests.get(
        f'http://proxy.tinsoftsv.com/api/getProxy.php?key={API_KEY}'
    )
    return recent_ip.json()
