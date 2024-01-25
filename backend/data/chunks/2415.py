    @app.get("/fast_uuid")
    def return_fast_uuid():
        asyncpg_uuid = MyUuid("a10ff360-3b1e-4984-a26f-d3ab460bdb51")
        assert isinstance(asyncpg_uuid, uuid.UUID)
        assert type(asyncpg_uuid) != uuid.UUID
        with pytest.raises(TypeError):
            vars(asyncpg_uuid)
        return {"fast_uuid": asyncpg_uuid}