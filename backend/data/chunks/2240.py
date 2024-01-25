def get_path_param_lt_int(item_id: int = Path(lt=3)):
    return item_id