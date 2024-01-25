    def model_fields(model: Type[BaseModel]) -> Dict[str, ModelField]:
        fields = {}
        for field_name, field in model.model_fields.items():
            fields[field_name] = ModelField(field_info=field, name=field_name)
        return fields