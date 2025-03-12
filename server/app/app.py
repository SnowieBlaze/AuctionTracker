from fastapi import FastAPI
from server.routes.auction.auction_get import auction_get

app = FastAPI()
app.include_router(auction_get, prefix="/auctions", tags=["auctions"])
@app.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server.app.app:app", host="127.0.0.1", port=8000, reload=True)
