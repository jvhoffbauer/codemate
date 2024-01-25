@app.get("/", response_class=PlainTextResponse)
async def main():
    return "Hello World"