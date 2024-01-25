@app.get("/users/{user_id}", dependencies=[Depends(user_exists)])
async def read_users(user_id: int):
    pass