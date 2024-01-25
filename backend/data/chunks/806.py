@app.get("/", include_in_schema=False)
def docs_redirect():
    return RedirectResponse(f"/docs")