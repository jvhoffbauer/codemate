@app.get("/users")
async def read_users():
    return ["Rick", "Morty"]