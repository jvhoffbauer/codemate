@app.post("/images/multiple/")
async def create_multiple_images(images: list[Image]):
    return images