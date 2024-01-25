@pytest.mark.asyncio
@pytest.mark.parametrize(*IO_PARAMS)
async def test_async_round_trip(tmp_path, name, content, kwargs):
    test_path = tmp_path / name
    assert not test_path.exists()

    await app.io.AIO.save(test_path, content, **kwargs)
    load_results = await app.io.AIO.load(test_path)
    assert load_results == content