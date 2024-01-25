    def __init__(
        self, model: Type[TableModelT] = None, fields: List[SqlaField] = None
    ) -> None:
        self.model = model or self.model
        assert self.model, "model is None"
        assert hasattr(
            self.model, "__table__"
        ), "model must be has __table__ attribute."
        self.pk_name: str = (
            self.pk_name or self.model.__table__.primary_key.columns.keys()[0]
        )
        self.pk: InstrumentedAttribute = self.model.__dict__[self.pk_name]
        self.parser = TableModelParser(self.model)
        fields = fields or self.fields or self.model_insfields
        exclude = self.parser.filter_insfield(self.exclude)
        self.fields = [
            sqlfield
            for sqlfield in self.parser.filter_insfield(
                fields + [self.pk], save_class=(Label,)
            )
            if sqlfield not in exclude
        ]
        assert self.fields, "fields is None"
        self.list_filter = self.list_filter and self.list_filter.copy() or self.fields
        self.link_models = self.link_models or {}
        """Make sure the value of link_models is an object attribute, not a class attribute."""