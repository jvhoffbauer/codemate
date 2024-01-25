def test_field_dict():
    class User(BaseModel):
        data: dict = Field({}, title="数据")

    modelfield = model_fields(User)["data"]
    assert modelfield
    # formitem
    formitem = amis_parser.as_form_item(modelfield)
    assert formitem.type == "json-editor"
    assert formitem.name == "data"
    column = amis_parser.as_table_column(modelfield)
    assert column.type == "json"
    assert column.label == "数据"