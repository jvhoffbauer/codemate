@app.get("/users")
async def read_users2():
    return ["Bean", "Elfo"]