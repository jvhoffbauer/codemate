    @app.post("/schema_extra/")
    def schema_extra(item: Item):
        return item