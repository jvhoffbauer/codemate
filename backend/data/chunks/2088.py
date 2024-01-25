@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}