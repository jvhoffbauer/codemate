    def sqlmodel_validate(
        cls: Type[_TSQLModel],
        obj: Any,
        *,
        strict: Union[bool, None] = None,
        from_attributes: Union[bool, None] = None,
        context: Union[Dict[str, Any], None] = None,
        update: Union[Dict[str, Any], None] = None,
    ) -> _TSQLModel:
        if not is_table_model_class(cls):
            new_obj: _TSQLModel = cls.__new__(cls)
        else:
            # If table, create the new instance normally to make SQLAlchemy create
            # the _sa_instance_state attribute
            # The wrapper of this function should use with _partial_init()
            with partial_init():
                new_obj = cls()
        # SQLModel Override to get class SQLAlchemy __dict__ attributes and
        # set them back in after creating the object
        old_dict = new_obj.__dict__.copy()
        use_obj = obj
        if isinstance(obj, dict) and update:
            use_obj = {**obj, **update}
        elif update:
            use_obj = ObjectWithUpdateWrapper(obj=obj, update=update)
        cls.__pydantic_validator__.validate_python(
            use_obj,
            strict=strict,
            from_attributes=from_attributes,
            context=context,
            self_instance=new_obj,
        )
        # Capture fields set to restore it later
        fields_set = new_obj.__pydantic_fields_set__.copy()
        if not is_table_model_class(cls):
            # If not table, normal Pydantic code, set __dict__
            new_obj.__dict__ = {**old_dict, **new_obj.__dict__}
        else:
            # Do not set __dict__, instead use setattr to trigger SQLAlchemy
            # instrumentation
            for key, value in {**old_dict, **new_obj.__dict__}.items():
                setattr(new_obj, key, value)
        # Restore fields set
        object.__setattr__(new_obj, "__pydantic_fields_set__", fields_set)
        # Get and set any relationship objects
        if is_table_model_class(cls):
            for key in new_obj.__sqlmodel_relationships__:
                value = getattr(use_obj, key, Undefined)
                if value is not Undefined:
                    setattr(new_obj, key, value)
        return new_obj