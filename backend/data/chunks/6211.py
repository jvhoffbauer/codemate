    def marge_model_config(
        model: Type[BaseModel], update: Dict[str, Any]
    ) -> Union[type, Dict[str, Any]]:
        return type("Config", (model.Config,), update)