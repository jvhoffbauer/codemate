@pytest.mark.asyncio
@pytest.mark.parametrize(*IO_PARAMS)
async def test_async_save(tmp_path, name, content, kwargs):
    test_path = tmp_path / name
    assert not test_path.exists()

    result = await app.io.AIO.save(test_path, content, **kwargs)
    assert result == test_path
    assert test_path.exists()