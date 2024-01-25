async def index(request: Request):
    return templates.TemplateResponse(
        "/whiteboard/index.html", {"request": request, "id": 1}
    )