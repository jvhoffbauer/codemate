@app.get("/hidden_header")
async def hidden_header(
    hidden_header: Optional[str] = Header(default=None, include_in_schema=False)
):
    return {"hidden_header": hidden_header}