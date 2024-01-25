def test_field_str():
    class User(BaseModel):
        name: str = Field("123456", title="姓名", min_length=2, max_length=10)

    modelfield = model_fields(User)["name"]
    # formitem
    formitem = amis_parser.as_form_item(modelfield, set_default=True)
    assert formitem.type == "input-text"
    assert formitem.label == "姓名"
    # assert formitem.minLength == 2  # type: ignore
    # assert formitem.maxLength == 10  # type: ignore
    assert formitem.value == "123456"
    # filter
    filteritem = amis_parser.as_form_item(modelfield, is_filter=True, set_default=True)
    assert filteritem.type == "input-text"
    assert filteritem.label == "姓名"
    assert hasattr(filteritem, "minLength") is False
    assert hasattr(filteritem, "maxLength") is False
    assert filteritem.value is None
    # table column
    column = amis_parser.as_table_column(modelfield)
    assert column.type is None
    assert column.label == "姓名"