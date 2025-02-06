import requests
import json

def get_auction_data():
    url = "https://api.hypixel.net/v2/skyblock/auctions"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data

data = get_auction_data()
last_time = 0
time = data["lastUpdated"]
auctions = data["auctions"]

def process_auctions():
    keys_to_keep = ["uuid", "start", "end", "item_name", "extra", "starting_bid", "bin"]
    filtered_auctions = [{key: auction[key] for key in keys_to_keep} for auction in auctions if auction.get("bin")]
    return filtered_auctions

print(process_auctions())