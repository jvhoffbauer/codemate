def resp_ok(*, code=0, msg="ok", data: Union[list, dict, str] = None) -> dict:
    return {"code": code, "msg": msg, "data": data}