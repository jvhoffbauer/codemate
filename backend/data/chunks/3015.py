@app.get("/")
def get_deps(dep1: str = Depends(get_header), dep2: str = Depends(get_something_else)):
    return {"dep1": dep1, "dep2": dep2}