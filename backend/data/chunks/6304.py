async def test_LinkAdmin(site: AdminSite):
    @site.register_admin
    class TmpAdmin(admin.LinkAdmin):
        link = "https://docs.amis.work"

    ins = site.get_admin_or_create(TmpAdmin)
    assert ins.page_schema.link == "https://docs.amis.work"