@app.get("/product")
async def create_item(product: Product):
    return product