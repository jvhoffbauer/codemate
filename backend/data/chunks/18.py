    def __setattr__(cls, name: str, value: Any) -> None:
        if is_table_model_class(cls):
            DeclarativeMeta.__setattr__(cls, name, value)
        else:
            super().__setattr__(name, value)