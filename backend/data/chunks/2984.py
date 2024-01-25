def put_invalid_user(
    user_id: str, name: str = Body(), db: dict = Depends(get_database)
):
    db[user_id] = name
    raise HTTPException(status_code=400, detail="Invalid user")