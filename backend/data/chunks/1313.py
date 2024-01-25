@app.post("/user/", response_model=UserOut)
async def create_user(user: UserIn) -> Any:
    return user