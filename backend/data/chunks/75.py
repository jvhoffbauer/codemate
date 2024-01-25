    def sqlmodel_init(*, self: "SQLModel", data: Dict[str, Any]) -> None:
        values, fields_set, validation_error = validate_model(self.__class__, data)
        # Only raise errors if not a SQLModel model
        if not is_table_model_class(self.__class__) and validation_error:  # noqa
            raise validation_error
        if not is_table_model_class(self.__class__):
            object.__setattr__(self, "__dict__", values)
        else:
            # Do not set values as in Pydantic, pass them through setattr, so
            # SQLAlchemy can handle them
            for key, value in values.items():
                setattr(self, key, value)
        object.__setattr__(self, "__fields_set__", fields_set)
        non_pydantic_keys = data.keys() - values.keys()

        if is_table_model_class(self.__class__):
            for key in non_pydantic_keys:
                if key in self.__sqlmodel_relationships__:
                    setattr(self, key, data[key])