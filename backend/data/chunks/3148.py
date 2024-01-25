@router_a.get("/override", response_class=PlainTextResponse)
def get_a_path_override():
    return "Hello A"