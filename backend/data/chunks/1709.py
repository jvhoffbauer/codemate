@app.get("/users/")
async def read_users(commons: CommonsDep):
    return commons