def test_field_model():
    class User(BaseModel):
        role: Role = Field(None, title="角色")
        roles: List[Role] = Field([], title="角色列表")

    modelfield = model_fields(User)["role"]
    assert modelfield
    # formitem
    formitem = amis_parser.as_form_item(modelfield, set_default=True)

    assert formitem.type == "input-sub-form"
    assert formitem.name == "role"
    assert formitem.label == "角色"
    assert formitem.form["body"][0]["name"] == "id"  # type: ignore
    assert formitem.form["body"][1]["name"] == "name"  # type: ignore

    modelfield = model_fields(User)["roles"]
    assert modelfield
    # formitem
    formitem = amis_parser.as_form_item(modelfield, set_default=True)
    assert formitem.type == "input-array"
    assert formitem.name == "roles"
    assert formitem.label == "角色列表"
    assert formitem.items.type == "input-sub-form"  # type: ignore
    assert formitem.items.labelField == "name"  # type: ignore