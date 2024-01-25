@app.get("/directCookie")
def get_direct_cookie(dep: str = Depends(set_cookie)):
    return {"dep": dep}