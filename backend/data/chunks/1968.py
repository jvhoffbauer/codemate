@app.get("/v2")
def read_main():
    return {"message": "Hello World"}