@app.get("/indirectCookie")
def get_indirect_cookie(dep: str = Depends(set_indirect_cookie)):
    return {"dep": dep}