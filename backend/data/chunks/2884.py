@item_router.get("/{item_id}")
def get_item(item_id: str, user_id: Optional[str] = None):
    if user_id is None:
        return {"item_id": item_id}
    else:
        return {"item_id": item_id, "user_id": user_id}