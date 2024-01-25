async def test_PageSchemaAdmin(site: AdminSite):
    @site.register_admin
    class TmpAdmin(admin.PageSchemaAdmin):
        pass

    ins = site.get_admin_or_create(TmpAdmin)
    assert ins.page_schema

    @site.register_admin
    class TmpAdmin1(admin.PageSchemaAdmin):
        page_schema = "page_label"

    ins = site.get_admin_or_create(TmpAdmin1)

    assert (
        isinstance(ins.page_schema, amis.PageSchema)
        and ins.page_schema.label == "page_label"
    )

    @site.register_admin
    class TmpAdmin2(admin.PageSchemaAdmin):
        page_schema = amis.PageSchema(label="page_label", isDefaultPage=True, sort=100)

    ins = site.get_admin_or_create(TmpAdmin2)

    assert (
        isinstance(ins.page_schema, amis.PageSchema)
        and ins.page_schema.label == "page_label"
    )