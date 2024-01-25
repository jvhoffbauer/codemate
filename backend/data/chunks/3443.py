@app.get("/hidden_cookie")
async def hidden_cookie(
    hidden_cookie: Optional[str] = Cookie(default=None, include_in_schema=False)
):
    return {"hidden_cookie": hidden_cookie}