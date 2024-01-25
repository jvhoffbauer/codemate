def get_site(*, alias: str = DEFAULT_ALIAS) -> AdminSite:
    """Get site"""
    return get_global(SITE_NAME, alias=alias)