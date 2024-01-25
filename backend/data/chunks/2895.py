@router.get("/users/{id}")
def read_user(segment: str, id: str):
    return {"segment": segment, "id": id}