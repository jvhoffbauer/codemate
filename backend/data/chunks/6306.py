async def test_IframeAdmin(site: AdminSite):
    @site.register_admin
    class TmpAdmin(admin.IframeAdmin):
        src = "https://docs.amis.work"

    ins = site.get_admin_or_create(TmpAdmin)
    assert (
        isinstance(ins.page_schema.schema_, amis.Iframe)
        and ins.page_schema.schema_.src == "https://docs.amis.work"
    )