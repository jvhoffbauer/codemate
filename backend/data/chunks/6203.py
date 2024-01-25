    def model_config_attr(
        model: Type[BaseModel], name: str, default: Any = None
    ) -> Any:
        return model.model_config.get(name, default)