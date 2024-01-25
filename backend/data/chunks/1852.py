@app.post("/images/multiple/")
async def create_multiple_images(images: List[Image]):
    return images