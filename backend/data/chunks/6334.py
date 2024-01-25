def test_field_enum():
    class UserStatus(str, Enum):
        NORMAL = "正常"
        DISABLED = "禁用"

    class User(BaseModel):
        status: Optional[UserStatus] = Field(None, title="状态")

    modelfield = model_fields(User)["status"]

    # formitem
    formitem = amis_parser.as_form_item(modelfield, set_default=True)
    assert formitem.type == "select"
    assert formitem.label == "状态"
    assert formitem.value is None
    assert formitem.options == [  # type: ignore
        {"label": "正常", "value": "正常"},
        {"label": "禁用", "value": "禁用"},
    ]
    # filter
    filteritem = amis_parser.as_form_item(modelfield, is_filter=True, set_default=True)
    assert filteritem.type == "select"
    assert filteritem.label == "状态"
    assert filteritem.value is None
    assert filteritem.options == [  # type: ignore
        {"label": "正常", "value": "正常"},
        {"label": "禁用", "value": "禁用"},
    ]
    # table column
    column = amis_parser.as_table_column(modelfield)
    assert column.type == "mapping"
    assert column.label == "状态"
    assert set(column.map.keys()) == {"正常", "禁用"}  # type: ignore