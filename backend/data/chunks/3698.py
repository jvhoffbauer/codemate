@app.get("/users/me")
def read_current_user(credentials: Optional[HTTPBasicCredentials] = Security(security)):
    if credentials is None:
        return {"msg": "Create an account first"}
    return {"username": credentials.username, "password": credentials.password}