@app.post("/users/", response_model=User)
async def create_user(user: UserCreate):
    return user