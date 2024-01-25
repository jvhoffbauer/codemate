    @app.post("/")
    def post_root(item1: Item):
        return item1  # pragma: nocover