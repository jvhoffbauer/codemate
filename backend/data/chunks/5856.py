    def __init__(
        self,
        model: Type[TableModelT],
        engine: SqlalchemyDatabase,
        fields: List[SqlaField] = None,
        router: APIRouter = None,
    ) -> None:
        self.engine = engine or self.engine
        assert self.engine, "engine is None"
        self.db = get_engine_db(self.engine)
        SqlalchemySelector.__init__(self, model, fields)
        schema_model: Type[
            SchemaModelT
        ] = self.schema_model or TableModelParser.get_table_model_schema(model)
        BaseCrud.__init__(self, schema_model, router)
        # if self.readonly_fields:
        #     logging.warning(
        #         "readonly fields, deprecated, not recommended, will be removed in version 0.4.0."
        #         "Please replace them with update_fields and update_exclude."
        #     )