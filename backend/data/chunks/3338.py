@router.route("/items/")
def read_items(request: Request):
    return JSONResponse({"hello": "world"})