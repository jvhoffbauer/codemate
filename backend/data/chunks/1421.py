@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}