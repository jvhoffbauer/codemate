@app.post("/user/")
async def create_user(user: UserIn) -> BaseUser:
    return user