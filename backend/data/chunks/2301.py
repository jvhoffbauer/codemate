    @app.post(
        "/",
        response_model=List[Item],
        responses={404: {"model": List[Message]}},
        generate_unique_id_function=custom_generate_unique_id3,
    )
    def post_root(item1: Item, item2: Item):
        return item1, item2  # pragma: nocover