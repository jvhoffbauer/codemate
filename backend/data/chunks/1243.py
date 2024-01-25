async def read_item(request: Request, id: str):
    return templates.TemplateResponse("item.html", {"request": request, "id": id})