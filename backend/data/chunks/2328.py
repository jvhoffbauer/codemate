def test_get_model_config():
    # For coverage in Pydantic v2
    class Foo(BaseModel):
        model_config = ConfigDict(from_attributes=True)

    foo = Foo()
    config = _get_model_config(foo)
    assert config == {"from_attributes": True}