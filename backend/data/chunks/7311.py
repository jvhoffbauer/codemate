def read_users(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
):
    """Retrieve users."""
    return crud.user.get_multi(db, skip=skip, limit=limit)