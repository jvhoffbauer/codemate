@router.post("/compute")
def compute(a: int = Body(), b: str = Body()):
    return {"a": a, "b": b}