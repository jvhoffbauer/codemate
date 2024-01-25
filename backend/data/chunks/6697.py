    def build_data_model(cls):
        if cls.DataModel is not None:
            return rename_if_scope_child_component(cls, cls.DataModel, "Data")

        error_model = cls.get_error_model()
        if error_model is None:
            return None

        default_value = ...
        errors_annotation = List[error_model]
        if not cls.errors_required:
            errors_annotation = Optional[errors_annotation]
            default_value = None

        field_definitions = {"errors": (errors_annotation, default_value)}

        name = f"_ErrorData[{error_model.__name__}]"
        _ErrorData = create_model(
            name,
            __base__=(BaseModel,),
            __module__=error_model.__module__,
            **field_definitions,
        )
        _ErrorData = component_name(name, error_model.__module__)(_ErrorData)

        return _ErrorData