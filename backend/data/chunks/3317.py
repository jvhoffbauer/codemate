def test_encode_deque_encodes_child_models():
    class Model(BaseModel):
        test: str

    dq = deque([Model(test="test")])

    assert jsonable_encoder(dq)[0]["test"] == "test"