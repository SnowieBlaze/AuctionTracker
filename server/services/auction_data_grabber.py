import requests
import json

def get_auction_data():
    url = "https://api.hypixel.net/v2/skyblock/auctions"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data