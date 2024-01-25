@app.get("/user")
def read_user(
    user_data: Tuple[str, List[str]] = Security(get_user, scopes=["foo", "bar"]),
    data: List[int] = Depends(get_data),
):
    return {"user": user_data[0], "scopes": user_data[1], "data": data}