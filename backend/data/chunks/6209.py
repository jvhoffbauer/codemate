    def model_fields(model: Type[BaseModel]) -> Dict[str, ModelField]:
        return model.__fields__