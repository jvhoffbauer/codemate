@app.get("/app")
def read_main():
    return {"message": "Hello World from main app"}