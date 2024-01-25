@app.get("/")
def root():
    return {"message": "Hello World"}