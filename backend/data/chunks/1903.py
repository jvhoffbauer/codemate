@app.get("/")
async def get():
    return HTMLResponse(html)