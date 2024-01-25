@app.get("/users/me")
# Here we use string annotations to test them
def read_current_user(current_user: "User" = Depends(get_current_user)):
    return current_user