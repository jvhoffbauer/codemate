@app.get("/users/")
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]