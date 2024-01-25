@app.post("/shops")
async def create_shop(
    data: Shop = Body(media_type=media_type),
    included: typing.List[Product] = Body(default=[], media_type=media_type),
):
    pass  # pragma: no cover