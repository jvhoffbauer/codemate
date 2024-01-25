@app.get("/users/")
def read_users():
    return ["Rick", "Morty"]