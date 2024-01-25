async def test_BaseAdmin(site: AdminSite):
    @site.register_admin
    class TmpAdmin(admin.BaseAdmin):
        pass

    ins = site.get_admin_or_create(TmpAdmin)
    assert ins.site is site
    assert ins.unique_id