@app.get("/typer")
async def redirect_typer():
    return RedirectResponse("https://typer.tiangolo.com")