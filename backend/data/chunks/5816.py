    def get_table_model_fields(table_model: Type[TableModelT]) -> Dict[str, ModelField]:
        """Get pydantic ModelField from sqlalchemy InspecTable."""
        if issubclass(table_model, BaseModel):
            return model_fields(table_model)
        elif hasattr(table_model, "__pydantic_model__") and issubclass(
            table_model.__pydantic_model__, BaseModel
        ):
            return model_fields(table_model.__pydantic_model__)
        return {}