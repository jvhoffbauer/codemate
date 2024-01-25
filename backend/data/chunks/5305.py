@bp.get("/test/1_plus_1_{result}")
def test_1_plus_1_v2(result: int):
    return {"result": result == 2}