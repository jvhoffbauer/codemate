async def test_form_admin_route_submit(site: AdminSite, async_client: AsyncClient):
    site.register_admin(TmpAdmin1)

    ins = site.get_admin_or_create(TmpAdmin1)

    site.register_router()
    # test form amis json
    res = await async_client.post(ins.router_path + ins.page_path)
    assert res.json()["data"]["body"]["type"] == "form"
    assert res.json()["data"]["body"]["api"]["url"] == ins.router_path + ins.form_path
    assert res.text.find("username") and res.text.find("password")
    # test form api submit
    data = {"username": "admin", "password": "admin"}
    res = await async_client.post(ins.router_path + ins.form_path, json=data)
    assert res.json()["data"] == {
        "username": "admin",
        "password": "admin",
        "extra": "success",
    }