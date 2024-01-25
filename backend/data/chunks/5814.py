    def get_table_model_insfields(
        table_model: Type[TableModelT],
    ) -> Dict[str, InstrumentedAttribute]:
        """Get sqlalchemy InstrumentedAttribute from InspecTable."""
        return {
            name: field
            for name, field in table_model.__dict__.items()
            if isinstance(field, InstrumentedAttribute)
        }