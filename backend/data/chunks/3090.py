@sub_router.get("/")
def read_item():
    return {"id": "foo"}