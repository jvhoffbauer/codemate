def register_model(schema: Type[SchemaT]):
    def decorator(model: Type[TableModelT]) -> Type[TableModelT]:
        model.__pydantic_model__ = schema
        return model

    return decorator