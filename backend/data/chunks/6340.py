def test_field_amis_extra_param():
    class User(BaseModel):
        field1: str = Field(
            ...,
            title="字段1",
            amis_form_item=amis.Textarea(),
            amis_filter_item={
                "type": "select",
                "options": [
                    {"label": "选项1", "value": "1"},
                    {"label": "选项2", "value": "2"},
                ],
            },
            amis_table_column=amis.TableColumn(type="audio", width=100),
        )
        field2: str = Field(
            ...,
            title="字段2",
            amis_form_item=lambda: amis.Textarea(),
            amis_filter_item=lambda: {
                "type": "select",
                "options": [
                    {"label": "选项1", "value": "1"},
                    {"label": "选项2", "value": "2"},
                ],
            },
        )

    modelfield = model_fields(User)["field1"]
    # formitem
    formitem = amis_parser.as_form_item(modelfield, set_default=True)
    assert formitem.name == "field1"
    assert formitem.type == "textarea"
    assert formitem.label == "字段1"

    # filter
    filteritem = amis_parser.as_form_item(modelfield, is_filter=True, set_default=True)
    assert filteritem.type == "select"
    assert filteritem.label == "字段1"

    # table column
    column = amis_parser.as_table_column(modelfield)
    assert column.type == "audio"
    assert column.width == 100

    modelfield2 = model_fields(User)["field2"]
    # formitem
    formitem = amis_parser.as_form_item(modelfield2, set_default=True)
    assert formitem.name == "field2"
    assert formitem.type == "textarea"
    assert formitem.label == "字段2"

    # filter
    filteritem = amis_parser.as_form_item(modelfield2, is_filter=True, set_default=True)
    assert filteritem.type == "select"
    assert filteritem.label == "字段2"