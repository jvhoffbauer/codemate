@pytest.fixture
def app() -> FastAPI:
    app = FastAPI()
    app.add_middleware(BaseHTTPMiddleware, dispatch=async_db.asgi_dispatch)
    return app