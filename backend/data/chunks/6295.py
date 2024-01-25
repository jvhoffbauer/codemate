async def test_get_model_admin(site: AdminSite, admin_cls_list, models):
    UserAdmin, BlogApp = admin_cls_list
    BlogApp.engine = create_engine("sqlite:///amisadmin2.db?check_same_thread=False")
    site.register_admin(BlogApp)
    site.register_router()
    assert site.get_model_admin(models.User.__tablename__) is None

    app = site.get_admin_or_create(BlogApp)
    assert app.get_model_admin(models.User.__tablename__)