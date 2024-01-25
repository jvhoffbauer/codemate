def get_item(*, db: Session = Depends(deps.get_db), id: int) -> models.Item:
    item = crud.item.get(db=db, id=id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found.")
    return item