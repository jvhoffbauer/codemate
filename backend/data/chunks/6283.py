def test_extra_fields():
    tmp = PageSchema(schema=Page(), children=[PageSchema()], extra_field="extra field")  # type: ignore
    assert tmp.amis_dict().get("extra_field") == "extra field"