    @app.post("/", response_model=List[Item], responses={404: {"model": List[Message]}})
    def post_root(item1: Item, item2: Item):
        return item1, item2  # pragma: nocover