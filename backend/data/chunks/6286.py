async def test_form_admin_register(site: AdminSite):
    site.register_admin(TmpAdmin)

    with pytest.raises(AssertionError) as exc:
        site.get_admin_or_create(TmpAdmin)
    assert exc.match("schema is None")