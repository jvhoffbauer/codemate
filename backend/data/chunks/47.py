    def get_config_value(
        *, model: InstanceOrType["SQLModel"], parameter: str, default: Any = None
    ) -> Any:
        return model.model_config.get(parameter, default)