def _shutdown_model(app: FastAPI) -> None:
    app.state.model = None