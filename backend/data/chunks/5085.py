@router.post("/", response_model=Item)
def create_item(
    *, item_in: ItemCreate, current_user: UserInDB = Depends(get_current_active_user)
):
    """
    Create new item.
    """
    bucket = get_default_bucket()
    id = crud.utils.generate_new_id()
    doc = crud.item.upsert(
        bucket=bucket, id=id, doc_in=item_in, owner_username=current_user.username
    )
    return doc