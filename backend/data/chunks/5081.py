@router.get("/", response_model=List[Item])
def read_items(
    skip: int = 0,
    limit: int = 100,
    current_user: UserInDB = Depends(get_current_active_user),
):
    """
    Retrieve items.

    If superuser, all the items.

    If normal user, the items owned by this user.
    """
    bucket = get_default_bucket()
    if crud.user.is_superuser(current_user):
        docs = crud.item.get_multi(bucket, skip=skip, limit=limit)
    else:
        docs = crud.item.get_multi_by_owner(
            bucket=bucket, owner_username=current_user.username, skip=skip, limit=limit
        )
    return docs