@bp.get("/test_1_plus_1/{result}")
def test_1_plus_1(result: int):
    return {"result": result == 2}