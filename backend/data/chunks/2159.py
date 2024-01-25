@app.post("/login")
def login(form_data: OAuth2PasswordRequestFormStrict = Depends()):
    return form_data