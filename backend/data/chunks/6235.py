def site() -> AdminSite:
    return AdminSite(settings=Settings(site_path=""), engine=async_db.engine)