@pytest.fixture
def app(ep):
    app = jsonrpc.API()
    app.bind_entrypoint(ep)
    return app