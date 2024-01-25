@app.post("/users/", response_model=UserBase)
async def create_user(user: UserCreate):
    return user