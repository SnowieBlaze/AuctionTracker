import requests
import json

def get_auction_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data