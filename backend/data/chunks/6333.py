def test_field_choices():
    class UserStatus(IntegerChoices):
        NORMAL = 1, "正常"
        DISABLED = 2, "禁用"

    class User(BaseModel):
        status: UserStatus = Field(UserStatus.NORMAL, title="状态")

    modelfield = model_fields(User)["status"]
    # formitem
    formitem = amis_parser.as_form_item(modelfield, set_default=True)
    assert formitem.type == "select"
    assert formitem.label == "状态"
    assert formitem.value == 1
    assert formitem.options == [  # type: ignore
        {"label": "正常", "value": 1},
        {"label": "禁用", "value": 2},
    ]
    # filter
    filteritem = amis_parser.as_form_item(modelfield, is_filter=True, set_default=True)
    assert filteritem.type == "select"
    assert filteritem.label == "状态"
    assert filteritem.value is None
    assert filteritem.options == [  # type: ignore
        {"label": "正常", "value": 1},
        {"label": "禁用", "value": 2},
    ]
    # table column
    column = amis_parser.as_table_column(modelfield)
    assert column.type == "mapping"
    assert column.label == "状态"
    assert set(column.map.keys()) == {1, 2}  # type: ignore