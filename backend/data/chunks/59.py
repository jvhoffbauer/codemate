    def sqlmodel_table_construct(
        *,
        self_instance: _TSQLModel,
        values: Dict[str, Any],
        _fields_set: Union[Set[str], None] = None,
    ) -> _TSQLModel:
        # Copy from Pydantic's BaseModel.construct()
        # Ref: https://github.com/pydantic/pydantic/blob/v2.5.2/pydantic/main.py#L198
        # Modified to not include everything, only the model fields, and to
        # set relationships
        # SQLModel override to get class SQLAlchemy __dict__ attributes and
        # set them back in after creating the object
        # new_obj = cls.__new__(cls)
        cls = type(self_instance)
        old_dict = self_instance.__dict__.copy()
        # End SQLModel override

        fields_values: Dict[str, Any] = {}
        defaults: Dict[
            str, Any
        ] = (
            {}
        )  # keeping this separate from `fields_values` helps us compute `_fields_set`
        for name, field in cls.model_fields.items():
            if field.alias and field.alias in values:
                fields_values[name] = values.pop(field.alias)
            elif name in values:
                fields_values[name] = values.pop(name)
            elif not field.is_required():
                defaults[name] = field.get_default(call_default_factory=True)
        if _fields_set is None:
            _fields_set = set(fields_values.keys())
        fields_values.update(defaults)

        _extra: Union[Dict[str, Any], None] = None
        if cls.model_config.get("extra") == "allow":
            _extra = {}
            for k, v in values.items():
                _extra[k] = v
        # SQLModel override, do not include everything, only the model fields
        # else:
        #     fields_values.update(values)
        # End SQLModel override
        # SQLModel override
        # Do not set __dict__, instead use setattr to trigger SQLAlchemy
        # object.__setattr__(new_obj, "__dict__", fields_values)
        # instrumentation
        for key, value in {**old_dict, **fields_values}.items():
            setattr(self_instance, key, value)
        # End SQLModel override
        object.__setattr__(self_instance, "__pydantic_fields_set__", _fields_set)
        if not cls.__pydantic_root_model__:
            object.__setattr__(self_instance, "__pydantic_extra__", _extra)

        if cls.__pydantic_post_init__:
            self_instance.model_post_init(None)
        elif not cls.__pydantic_root_model__:
            # Note: if there are any private attributes, cls.__pydantic_post_init__ would exist
            # Since it doesn't, that means that `__pydantic_private__` should be set to None
            object.__setattr__(self_instance, "__pydantic_private__", None)
        # SQLModel override, set relationships
        # Get and set any relationship objects
        for key in self_instance.__sqlmodel_relationships__:
            value = values.get(key, Undefined)
            if value is not Undefined:
                setattr(self_instance, key, value)
        # End SQLModel override
        return self_instance