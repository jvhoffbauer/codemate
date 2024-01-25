def get_path_param_lt_gt_int(item_id: int = Path(lt=3, gt=1)):
    return item_id