@app.put("/user/{user_id}")
def put_user(user_id: str, name: str = Body(), db: dict = Depends(get_database)):
    db[user_id] = name
    return {"message": "OK"}