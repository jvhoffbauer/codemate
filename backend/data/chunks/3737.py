def test_router_events(state: State) -> None:
    app = FastAPI()

    @app.get("/")
    def main() -> Dict[str, str]:
        return {"message": "Hello World"}

    @app.on_event("startup")
    def app_startup() -> None:
        state.app_startup = True

    @app.on_event("shutdown")
    def app_shutdown() -> None:
        state.app_shutdown = True

    router = APIRouter()

    @router.on_event("startup")
    def router_startup() -> None:
        state.router_startup = True

    @router.on_event("shutdown")
    def router_shutdown() -> None:
        state.router_shutdown = True

    sub_router = APIRouter()

    @sub_router.on_event("startup")
    def sub_router_startup() -> None:
        state.sub_router_startup = True

    @sub_router.on_event("shutdown")
    def sub_router_shutdown() -> None:
        state.sub_router_shutdown = True

    router.include_router(sub_router)
    app.include_router(router)

    assert state.app_startup is False
    assert state.router_startup is False
    assert state.sub_router_startup is False
    assert state.app_shutdown is False
    assert state.router_shutdown is False
    assert state.sub_router_shutdown is False
    with TestClient(app) as client:
        assert state.app_startup is True
        assert state.router_startup is True
        assert state.sub_router_startup is True
        assert state.app_shutdown is False
        assert state.router_shutdown is False
        assert state.sub_router_shutdown is False
        response = client.get("/")
        assert response.status_code == 200, response.text
        assert response.json() == {"message": "Hello World"}
    assert state.app_startup is True
    assert state.router_startup is True
    assert state.sub_router_startup is True
    assert state.app_shutdown is True
    assert state.router_shutdown is True
    assert state.sub_router_shutdown is True