    @app.post("/items-list/")
    def create_item_list(item: List[Item]):
        return item