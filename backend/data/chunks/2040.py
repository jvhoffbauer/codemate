@app.get("/items/", response_class=HTMLResponse)
async def read_items():
    return generate_html_response()