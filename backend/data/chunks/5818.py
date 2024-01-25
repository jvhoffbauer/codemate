    def get_table_model_schema(
        table_model: Type[TableModelT],
    ) -> Optional[Type[BaseModel]]:
        """Get pydantic schema from sqlalchemy InspecTable."""

        if issubclass(table_model, BaseModel):
            return table_model
        elif hasattr(table_model, "__pydantic_model__") and issubclass(
            table_model.__pydantic_model__, BaseModel
        ):
            return table_model.__pydantic_model__
        insfields = TableModelParser.get_table_model_insfields(table_model)
        if not insfields:
            return None
        modelfields = [
            insfield_to_modelfield(insfield) for insfield in insfields.values()
        ]
        modelfields = list(filter(None, modelfields))
        table_model.__pydantic_model__ = create_model_by_fields(
            table_model.__name__, modelfields, orm_mode=True
        )
        return table_model.__pydantic_model__