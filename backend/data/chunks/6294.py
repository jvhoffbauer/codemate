async def test_register_admin(site: AdminSite, admin_cls_list, models):
    UserAdmin, BlogApp = admin_cls_list
    app = site.get_admin_or_create(BlogApp)
    assert app.db
    assert app.engine
    ins = app.get_admin_or_create(UserAdmin)
    assert ins in app
    assert app.get_model_admin(models.User.__tablename__)

    site.register_router()
    assert site.get_model_admin(models.User.__tablename__)

    site.unregister_admin(BlogApp)
    app = site.get_admin_or_create(BlogApp, register=False)
    assert app is None