def create_bp(dependencies: list = None) -> FastAPIPlus:
    if not dependencies:
        dependencies = []
    app = FastAPIPlus(dependencies=dependencies)
    setup_error_handlers(app)
    return app