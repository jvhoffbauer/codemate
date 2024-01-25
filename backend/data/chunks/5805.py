def parser_str_set_list(item_id: Union[int, str]) -> List[str]:
    if isinstance(item_id, int):
        return [str(item_id)]
    elif not isinstance(item_id, str) or not item_id:
        return []
    return list(set(item_id.split(",")))