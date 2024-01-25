def get_path_param_le_int(item_id: int = Path(le=3)):
    return item_id