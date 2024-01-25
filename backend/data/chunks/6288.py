async def test_form_admin_route_init(site: AdminSite, async_client: AsyncClient):
    site.register_admin(TmpAdmin2)

    ins = site.get_admin_or_create(TmpAdmin2)

    site.register_router()
    # test form amis json
    res = await async_client.post(ins.router_path + ins.page_path)
    assert res.json()["data"]["body"]["type"] == "form"
    assert (
        res.json()["data"]["body"]["initApi"]["url"] == ins.router_path + ins.form_path
    )
    assert res.text.find("username") and res.text.find("password")
    # test form api init
    data = {"username": "admin", "password": "admin"}
    res = await async_client.get(ins.router_path + ins.form_path)
    assert res.json()["data"] == data