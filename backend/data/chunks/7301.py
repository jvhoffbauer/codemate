@router.post("/", response_model=schemas.Item)
def create_item(
    *,
    db: Session = Depends(deps.get_db),
    item_in: schemas.ItemCreate,
    user: models.User = Depends(deps.get_current_active_user),
):
    """Create new item."""
    return crud.item.create_with_owner(db, obj_in=item_in, owner_id=user.id)