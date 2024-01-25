@needs_pydanticv1
def test_pydanticv1():
    app = FastAPI()

    @app.get("/fast_uuid")
    def return_fast_uuid():
        asyncpg_uuid = MyUuid("a10ff360-3b1e-4984-a26f-d3ab460bdb51")
        assert isinstance(asyncpg_uuid, uuid.UUID)
        assert type(asyncpg_uuid) != uuid.UUID
        with pytest.raises(TypeError):
            vars(asyncpg_uuid)
        return {"fast_uuid": asyncpg_uuid}

    class SomeCustomClass(BaseModel):
        class Config:
            arbitrary_types_allowed = True
            json_encoders = {uuid.UUID: str}

        a_uuid: MyUuid

    @app.get("/get_custom_class")
    def return_some_user():
        # Test that the fix also works for custom pydantic classes
        return SomeCustomClass(a_uuid=MyUuid("b8799909-f914-42de-91bc-95c819218d01"))

    client = TestClient(app)

    with client:
        response_simple = client.get("/fast_uuid")
        response_pydantic = client.get("/get_custom_class")

    assert response_simple.json() == {
        "fast_uuid": "a10ff360-3b1e-4984-a26f-d3ab460bdb51"
    }

    assert response_pydantic.json() == {
        "a_uuid": "b8799909-f914-42de-91bc-95c819218d01"
    }