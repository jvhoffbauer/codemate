    def get_config_value(
        *, model: InstanceOrType["SQLModel"], parameter: str, default: Any = None
    ) -> Any:
        return getattr(model.__config__, parameter, default)  # type: ignore[union-attr]