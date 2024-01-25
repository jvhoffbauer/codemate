async def get_db():
    with MySuperContextManager() as db:
        yield db