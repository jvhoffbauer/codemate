    def decorator(obj):
        assert issubclass(obj, BaseModel)
        opts = {
            "__base__": tuple(obj.mro()[1:]),  # remove self from __base__
            "__module__": module or obj.__module__,
            **{
                field_name: (field.annotation, field)
                for field_name, field in obj.model_fields.items()
            },
        }
        if obj.model_config:
            opts.pop("__base__")
            opts["__config__"] = obj.model_config

        # re-create model to ensure given name will be applied to json schema
        # since Pydantic 2.0 model json schema generated at class creation process

        obj = create_model(name, **opts)

        if module is not None:
            obj.__module__ = module  # see: pydantic._internal._core_utils.get_type_ref
        key = (obj.__name__, obj.__module__)
        if key in components:
            lhs = components[key].model_json_schema()
            rhs = obj.model_json_schema()
            if lhs != rhs:
                raise RuntimeError(
                    f"Different models with the same name detected: {lhs!r} != {rhs}"
                )
            return components[key]
        components[key] = obj
        return obj