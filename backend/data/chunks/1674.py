@app.get("/")
async def root():
    return {"message": "Hello World"}