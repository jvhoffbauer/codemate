        def get_config(name: str) -> Any:
            config_class_value = get_config_value(
                model=new_cls, parameter=name, default=Undefined
            )
            if config_class_value is not Undefined:
                return config_class_value
            kwarg_value = kwargs.get(name, Undefined)
            if kwarg_value is not Undefined:
                return kwarg_value
            return Undefined