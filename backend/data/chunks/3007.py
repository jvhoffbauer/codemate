@app.post("/login")
# Here we use string annotations to test them
def login(form_data: "OAuth2PasswordRequestFormStrict" = Depends()):
    return form_data