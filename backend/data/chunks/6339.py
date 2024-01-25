def test_field_param_alias():
    class User(BaseModel):
        name: str = Field(..., title="姓名", alias="username")
        role: Role = Field(None, title="角色", alias="user_role")

    modelfield = model_fields(User)["name"]
    # formitem
    formitem = amis_parser.as_form_item(modelfield, set_default=True)
    assert formitem.name == "username"

    role_field = model_fields(User)["role"]
    # formitem
    formitem = amis_parser.as_form_item(role_field, set_default=True)
    assert formitem.name == "user_role"