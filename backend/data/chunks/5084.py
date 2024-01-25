def search_items(
    q: str,
    skip: int = 0,
    limit: int = 100,
    current_user: UserInDB = Depends(get_current_active_user),
):
    """
    Search items, use Bleve Query String syntax:
    http://blevesearch.com/docs/Query-String-Query/

    For typeahead suffix with `*`. For example, a query with: `title:foo*` will match
    items containing `football`, `fool proof`, etc.
    """
    bucket = get_default_bucket()
    if crud.user.is_superuser(current_user):
        docs = crud.item.search(bucket=bucket, query_string=q, skip=skip, limit=limit)
    else:
        docs = crud.item.search_with_owner(
            bucket=bucket,
            query_string=q,
            username=current_user.username,
            skip=skip,
            limit=limit,
        )
    return docs