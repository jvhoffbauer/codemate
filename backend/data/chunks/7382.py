def resp_fail(*, code=1, msg="fail", data: Union[list, dict, str] = None):
    return {"code": code, "msg": msg, "data": data}