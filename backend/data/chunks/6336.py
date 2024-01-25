def test_field_list():
    class User(BaseModel):
        tags: List[str] = Field([], title="标签")
        email: List[str] = Field(
            [],
            title="邮箱列表",
            amis_form_item=amis.InputArray(items=amis.InputText(type="input-email")),
        )
        names: list = Field([], title="姓名列表")

    # test tags
    modelfield = model_fields(User)["tags"]
    assert modelfield
    # formitem
    formitem = amis_parser.as_form_item(modelfield, set_default=True)
    assert formitem.type == "input-array"
    assert formitem.name == "tags"
    assert formitem.label == "标签"
    assert formitem.value == []
    assert formitem.items.type == "input-text"  # type: ignore

    # test email
    modelfield = model_fields(User)["email"]
    assert modelfield
    # formitem
    formitem = amis_parser.as_form_item(modelfield)
    assert formitem.type == "input-array"
    assert formitem.name == "email"
    assert formitem.items.type == "input-email"  # type: ignore

    # test names
    modelfield = model_fields(User)["names"]
    assert modelfield
    # formitem
    formitem = amis_parser.as_form_item(modelfield)
    assert formitem.type == "input-array"
    assert formitem.name == "names"