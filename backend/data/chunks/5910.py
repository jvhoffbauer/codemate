    def __init__(self, schema_model: Type[SchemaModelT], router: APIRouter = None):
        self.paginator = Paginator()
        self.schema_model = schema_model or self.schema_model
        assert self.schema_model, "schema_model is None"
        self.router = router
        RouterMixin.__init__(self)