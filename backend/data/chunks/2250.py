def get_path_param_le_ge_int(item_id: int = Path(le=3, ge=1)):
    return item_id