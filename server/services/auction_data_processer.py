def process_auctions(auctions, keys_to_keep):
    return [
        {key: auction[key] for key in keys_to_keep} for auction in auctions
    ]


def filter_auction_minimum_bid(auctions, min_val):
    return [
        auction for auction in auctions
        if auction.get("bin") and auction.get("starting_bid", 0) >= min_val
    ]
