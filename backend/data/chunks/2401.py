@app.get("/items/")
async def read_items(token: Optional[str] = Security(oauth2_scheme)):
    if token is None:
        return {"msg": "Create an account first"}
    return {"token": token}