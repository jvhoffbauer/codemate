@app.get("/")
def get_root():
    return {"msg": "Hello World"}