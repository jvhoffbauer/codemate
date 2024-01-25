def test_field_bool():
    class User(BaseModel):
        is_admin: bool = Field(True, title="是否管理员")

    modelfield = model_fields(User)["is_admin"]
    # formitem
    formitem = amis_parser.as_form_item(modelfield, set_default=True)
    assert formitem.type == "switch"
    assert formitem.label == "是否管理员"
    assert formitem.value
    # filter
    filteritem = amis_parser.as_form_item(modelfield, is_filter=True, set_default=True)
    assert filteritem.type == "switch"
    assert filteritem.label == "是否管理员"
    assert filteritem.value is None
    # table column
    column = amis_parser.as_table_column(modelfield)
    assert column.type == "switch"
    assert column.label == "是否管理员"