@router_b_a_c_override.get("/override", response_class=OverrideResponse)
def get_b_a_c_path_override():
    return {"msg": "Hello B A C"}