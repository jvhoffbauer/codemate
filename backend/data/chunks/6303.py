    @site.register_admin
    class TmpAdmin2(admin.PageSchemaAdmin):
        page_schema = amis.PageSchema(label="page_label", isDefaultPage=True, sort=100)