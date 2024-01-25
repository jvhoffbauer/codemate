    def model_config_attr(
        model: Type[BaseModel], name: str, default: Any = None
    ) -> Any:
        return getattr(model.Config, name, default)