@app.get("/path/param-le/{item_id}")
def get_path_param_le(item_id: float = Path(le=3)):
    return item_id