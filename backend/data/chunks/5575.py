def CustomPathParams(
    name: str = Query(
        ...,
        alias="file",
        description="Give me a url.",
    )
) -> str:
    """Custom path Dependency."""
    if not re.match(".+tif$", name):
        raise HTTPException(
            status_code=400,
            detail="Nope, this is not a valid File - Please Try Again",
        )

    if not os.path.exists(f"{DATA_DIR}/{name}"):
        raise HTTPException(
            status_code=404,
            detail="The File doesn't exists - Please Try Again",
        )

    return f"{DATA_DIR}/{name}"