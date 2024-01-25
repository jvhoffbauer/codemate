    @router.post(
        "/router", response_model=List[Item], responses={404: {"model": List[Message]}}
    )
    def post_router(item1: Item, item2: Item):
        return item1, item2  # pragma: nocover