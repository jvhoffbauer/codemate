def set_site(
    site: AdminSite,
    *,
    alias: str = DEFAULT_ALIAS,
    overwrite: bool = False,
) -> bool:
    """Set site"""
    return set_global(SITE_NAME, site, alias=alias, overwrite=overwrite)