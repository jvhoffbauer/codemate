@app.get("/path/param/{item_id}")
def get_path_param_id(item_id: Optional[str] = Path()):
    return item_id