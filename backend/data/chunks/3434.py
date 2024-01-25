def test_nested_router():
    app = FastAPI()

    router = APIRouter(prefix="/nested")

    @router.get("/test")
    async def test(var: Annotated[str, Query()] = "bar"):
        return {"foo": var}

    app.include_router(router)

    client = TestClient(app)

    response = client.get("/nested/test")
    assert response.status_code == 200
    assert response.json() == {"foo": "bar"}