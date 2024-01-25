@app.get("/users/", tags=[Tags.users])
async def read_users():
    return ["Rick", "Morty"]