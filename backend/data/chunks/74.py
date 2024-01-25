    def sqlmodel_validate(
        cls: Type[_TSQLModel],
        obj: Any,
        *,
        strict: Union[bool, None] = None,
        from_attributes: Union[bool, None] = None,
        context: Union[Dict[str, Any], None] = None,
        update: Union[Dict[str, Any], None] = None,
    ) -> _TSQLModel:
        # This was SQLModel's original from_orm() for Pydantic v1
        # Duplicated from Pydantic
        if not cls.__config__.orm_mode:  # type: ignore[attr-defined] # noqa
            raise ConfigError(
                "You must have the config attribute orm_mode=True to use from_orm"
            )
        if not isinstance(obj, Mapping):
            obj = (
                {ROOT_KEY: obj}
                if cls.__custom_root_type__  # type: ignore[attr-defined] # noqa
                else cls._decompose_class(obj)  # type: ignore[attr-defined] # noqa
            )
        # SQLModel, support update dict
        if update is not None:
            obj = {**obj, **update}
        # End SQLModel support dict
        if not getattr(cls.__config__, "table", False):  # noqa
            # If not table, normal Pydantic code
            m: _TSQLModel = cls.__new__(cls)
        else:
            # If table, create the new instance normally to make SQLAlchemy create
            # the _sa_instance_state attribute
            m = cls()
        values, fields_set, validation_error = validate_model(cls, obj)
        if validation_error:
            raise validation_error
        # Updated to trigger SQLAlchemy internal handling
        if not getattr(cls.__config__, "table", False):  # noqa
            object.__setattr__(m, "__dict__", values)
        else:
            for key, value in values.items():
                setattr(m, key, value)
        # Continue with standard Pydantic logic
        object.__setattr__(m, "__fields_set__", fields_set)
        m._init_private_attributes()  # type: ignore[attr-defined] # noqa
        return m