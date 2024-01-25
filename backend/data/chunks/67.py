    def is_table_model_class(cls: Type[Any]) -> bool:
        config = getattr(cls, "__config__", None)
        if config:
            return getattr(config, "table", False)
        return False