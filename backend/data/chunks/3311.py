@needs_pydanticv1
def test_encode_root():
    class ModelWithRoot(BaseModel):
        __root__: str

    model = ModelWithRoot(__root__="Foo")
    assert jsonable_encoder(model) == "Foo"