@app.get("/override", response_class=PlainTextResponse)
def get_path_override():
    return "Hello World"