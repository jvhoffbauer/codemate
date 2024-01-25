@app.get("/")
async def main():
    return {"message": "Hello World"}