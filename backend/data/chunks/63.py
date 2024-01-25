    def set_config_value(
        *,
        model: InstanceOrType["SQLModel"],
        parameter: str,
        value: Any,
    ) -> None:
        setattr(model.__config__, parameter, value)  # type: ignore