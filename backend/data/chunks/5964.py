def exists_site(*, alias: str = DEFAULT_ALIAS) -> bool:
    """Judge whether the site exists"""
    return exists_global(SITE_NAME, alias=alias)