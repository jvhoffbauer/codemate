    def set_config_value(
        *,
        model: InstanceOrType["SQLModel"],
        parameter: str,
        value: Any,
    ) -> None:
        model.model_config[parameter] = value  # type: ignore[literal-required]