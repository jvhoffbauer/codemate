@app.post("/products")
async def create_product(data: Product = Body(media_type=media_type, embed=True)):
    pass  # pragma: no cover