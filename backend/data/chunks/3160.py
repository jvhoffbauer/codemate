@router_b_override.get("/override", response_class=HTMLResponse)
def get_b_path_override():
    return "Hello B"