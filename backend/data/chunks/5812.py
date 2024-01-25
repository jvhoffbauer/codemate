    def __init__(self, table_model: Type[TableModelT]):
        assert hasattr(
            table_model, "__table__"
        ), "table_model must be has __table__ attribute."
        self.table_model = table_model
        self.__table__: Table = self.table_model.__table__  # type: ignore
        self.__fields__ = self.get_table_model_fields(table_model)