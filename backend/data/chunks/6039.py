    def __init__(self, app: "AdminApp"):
        assert self.model, "model is None"
        assert app, "app is None"
        self.app = app
        self.engine = self.engine or self.app.engine
        self.amis_parser = self.app.site.amis_parser
        self.parser = TableModelParser(self.model)
        self.schema_model = self.parser.get_table_model_schema(self.model)
        assert self.schema_model, "schema_model is None"
        list_display_insfield = self.parser.filter_insfield(
            self.list_display, save_class=(Label,)
        )
        self.list_filter = (
            self.list_filter and self.list_filter.copy() or list_display_insfield or []
        )
        self.list_filter.extend(
            [field for field in self.search_fields if field not in self.list_filter]
        )
        SqlalchemyCrud.__init__(self, self.model, self.engine)
        self.fields.extend(list_display_insfield)
        BaseActionAdmin.__init__(self, app)