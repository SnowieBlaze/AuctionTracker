from fastapi import APIRouter
from fastapi.concurrency import run_in_threadpool
from server.config import AUCTION_URL
from server.services.auction_data_grabber import get_auction_data

auction_get = APIRouter()

@auction_get.get("/")
async def get_auctions():
    auctions = await run_in_threadpool(get_auction_data, AUCTION_URL)
    if auctions:
        auctions = auctions.get("auctions", [])
        return {"auctions": auctions}
    else:
        return {"error": "Failed to get auctions"}, 500


# @auction_get.get("/{id}")
# async def get_auction_by_id(id: int):
#     auctions = await run_in_threadpool(get_auction_data, AUCTION_URL)
#     auctions = auctions.get("auctions", [])
#     if auctions and 0 <= id < len(auctions):
#         return auctions[id]
#     else:
#         return {"error": "Auction not found or invalid ID."}, 404

