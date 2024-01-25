@user_router.get("/{user_id}")
def get_user(user_id: str):
    return {"user_id": user_id}