def get_valid_none(send_none: bool = False):
    if send_none:
        return None
    else:
        return {"name": "invalid", "price": 3.2}