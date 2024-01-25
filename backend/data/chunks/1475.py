@app.get("/users/", tags=["users"])
async def read_users():
    return [{"username": "johndoe"}]