@router_a_b_override.get("/override", response_class=HTMLResponse)
def get_a_b_path_override():
    return "Hello A B"