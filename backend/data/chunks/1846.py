@app.post("/offers/")
async def create_offer(offer: Offer):
    return offer