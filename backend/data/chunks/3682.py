def get_app_client(separate_input_output_schemas: bool = True) -> TestClient:
    app = FastAPI(separate_input_output_schemas=separate_input_output_schemas)

    @app.post("/items/")
    def create_item(item: Item):
        return item

    @app.post("/items-list/")
    def create_item_list(item: List[Item]):
        return item

    @app.get("/items/")
    def read_items() -> List[Item]:
        return [
            Item(
                name="Portal Gun",
                description="Device to travel through the multi-rick-verse",
                sub=SubItem(subname="subname"),
            ),
            Item(name="Plumbus"),
        ]

    client = TestClient(app)
    return client