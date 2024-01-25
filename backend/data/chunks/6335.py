def test_field_datetime():
    from datetime import datetime

    class User(BaseModel):
        created_at: datetime = Field(None, title="创建时间")

    modelfield = model_fields(User)["created_at"]
    # formitem
    formitem = amis_parser.as_form_item(modelfield, set_default=True)
    assert formitem.type == "input-datetime"
    assert formitem.label == "创建时间"
    # filter
    filteritem = amis_parser.as_form_item(modelfield, is_filter=True, set_default=True)
    assert filteritem.type == "input-datetime-range"
    assert filteritem.label == "创建时间"
    assert filteritem.value is None
    # table column
    column = amis_parser.as_table_column(modelfield)
    assert column.type == "datetime"
    assert column.label == "创建时间"