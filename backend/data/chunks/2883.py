def get_items(user_id: Optional[str] = None):
    if user_id is None:
        return [{"item_id": "i1", "user_id": "u1"}, {"item_id": "i2", "user_id": "u2"}]
    else:
        return [{"item_id": "i2", "user_id": user_id}]