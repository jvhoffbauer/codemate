    def is_table_model_class(cls: Type[Any]) -> bool:
        config = getattr(cls, "model_config", {})
        if config:
            return config.get("table", False) or False
        return False