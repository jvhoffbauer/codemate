def test_encode_model_with_pure_path():
    class ModelWithPath(BaseModel):
        path: PurePath

        if PYDANTIC_V2:
            model_config = {"arbitrary_types_allowed": True}
        else:

            class Config:
                arbitrary_types_allowed = True

    test_path = PurePath("/foo", "bar")
    obj = ModelWithPath(path=test_path)
    assert jsonable_encoder(obj) == {"path": str(test_path)}