def test_app_lifespan_state(state: State) -> None:
    @asynccontextmanager
    async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
        state.app_startup = True
        yield
        state.app_shutdown = True

    app = FastAPI(lifespan=lifespan)

    @app.get("/")
    def main() -> Dict[str, str]:
        return {"message": "Hello World"}

    assert state.app_startup is False
    assert state.app_shutdown is False
    with TestClient(app) as client:
        assert state.app_startup is True
        assert state.app_shutdown is False
        response = client.get("/")
        assert response.status_code == 200, response.text
        assert response.json() == {"message": "Hello World"}
    assert state.app_startup is True
    assert state.app_shutdown is True