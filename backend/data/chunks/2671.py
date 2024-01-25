def set_indirect_cookie(*, dep: str = Depends(set_cookie)):
    return dep