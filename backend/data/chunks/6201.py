    def model_config(model: Type[BaseModel]) -> Union[type, Dict[str, Any]]:
        return model.model_config