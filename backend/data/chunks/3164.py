@router_b_a.get("/override", response_class=HTMLResponse)
def get_b_a_path_override():
    return "Hello B A"