def test_field_int():
    class User(BaseModel):
        age: int = Field(18, title="年龄")

    modelfield = model_fields(User)["age"]
    # formitem
    formitem = amis_parser.as_form_item(modelfield, set_default=True)
    assert formitem.type == "input-number"
    assert formitem.label == "年龄"
    assert formitem.value == 18
    # filter
    filteritem = amis_parser.as_form_item(modelfield, is_filter=True, set_default=True)
    assert filteritem.type == "input-text"  # 搜索时,数字类型的字段使用文本框.可使用[>,<,>=,<=,!=]等符号.
    assert filteritem.label == "年龄"
    assert filteritem.value is None
    # table column
    column = amis_parser.as_table_column(modelfield)
    assert column.type is None
    assert column.label == "年龄"