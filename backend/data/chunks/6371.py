@pytest.fixture
def app() -> FastAPI:
    app = FastAPI()
    app.add_middleware(BaseHTTPMiddleware, dispatch=db.asgi_dispatch)
    return app