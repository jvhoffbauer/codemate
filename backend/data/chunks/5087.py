@router.put("/{id}", response_model=Item)
def update_item(
    *,
    id: str,
    item_in: ItemUpdate,
    current_user: UserInDB = Depends(get_current_active_user),
):
    """
    Update an item.
    """
    bucket = get_default_bucket()
    doc = crud.item.get(bucket=bucket, id=id)
    if not doc:
        raise HTTPException(status_code=404, detail="Item not found")
    if not crud.user.is_superuser(current_user) and (
        doc.owner_username != current_user.username
    ):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    doc = crud.item.update(
        bucket=bucket, id=id, doc_in=item_in, owner_username=doc.owner_username
    )
    return doc