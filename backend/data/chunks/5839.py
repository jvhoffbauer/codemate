    def decorator(model: Type[TableModelT]) -> Type[TableModelT]:
        model.__pydantic_model__ = schema
        return model