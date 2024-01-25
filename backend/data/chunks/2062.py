@subapi.get("/sub")
def read_sub():
    return {"message": "Hello World from sub API"}