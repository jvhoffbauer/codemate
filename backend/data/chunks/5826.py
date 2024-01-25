    def get_insfield(self, field: SqlaInsAttr) -> Optional[InstrumentedAttribute]:
        if isinstance(field, str):
            field = self.table_model.__dict__.get(field, None)
        if isinstance(field, InstrumentedAttribute):
            return field
        return None