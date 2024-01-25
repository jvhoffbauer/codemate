@router.get("/search/", response_model=List[User])
def search_users(
    q: str,
    skip: int = 0,
    limit: int = 100,
    current_user: UserInDB = Depends(get_current_active_superuser),
):
    """
    Search users, use Bleve Query String syntax:
    http://blevesearch.com/docs/Query-String-Query/

    For typeahead suffix with `*`. For example, a query with: `email:johnd*` will match
    users with email `johndoe@example.com`, `johndid@example.net`, etc.
    """
    bucket = get_default_bucket()
    users = crud.user.search(bucket=bucket, query_string=q, skip=skip, limit=limit)
    return users