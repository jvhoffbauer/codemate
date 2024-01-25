    def __delattr__(cls, name: str) -> None:
        if is_table_model_class(cls):
            DeclarativeMeta.__delattr__(cls, name)
        else:
            super().__delattr__(name)