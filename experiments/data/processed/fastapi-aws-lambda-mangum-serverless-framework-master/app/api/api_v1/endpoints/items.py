from fastapi import APIRouter

router = APIRouter()

@router.get("/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}