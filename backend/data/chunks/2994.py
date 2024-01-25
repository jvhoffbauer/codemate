def test_include_empty():
    # if both include and router.path are empty - it should raise exception
    with pytest.raises(FastAPIError):
        app.include_router(router)