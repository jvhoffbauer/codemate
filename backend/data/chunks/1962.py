@app.get("/")
async def root():
    return {"message": "Tomato"}