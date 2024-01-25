@router.get("/{id}", response_model=Item)
def read_item(id: str, current_user: UserInDB = Depends(get_current_active_user)):
    """
    Get item by ID.
    """
    bucket = get_default_bucket()
    doc = crud.item.get(bucket=bucket, id=id)
    if not doc:
        raise HTTPException(status_code=404, detail="Item not found")
    if not crud.user.is_superuser(current_user) and (
        doc.owner_username != current_user.username
    ):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return doc