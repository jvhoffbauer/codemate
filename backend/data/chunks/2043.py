@app.get("/", response_class=CustomORJSONResponse)
async def main():
    return {"message": "Hello World"}