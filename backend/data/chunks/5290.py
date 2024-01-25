@bp.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        "/whiteboard/index.html", {"request": request, "id": 1}
    )