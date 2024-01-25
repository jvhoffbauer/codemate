    @app.post("/second")
    def post_second(item1: Item):
        return item1  # pragma: nocover