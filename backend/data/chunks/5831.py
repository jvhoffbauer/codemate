def _get_label_modelfield(label: Label) -> ModelField:
    modelfield = getattr(label, "__ModelField__", None)
    if modelfield is None:
        try:
            type_ = label.expression.type.python_type
        except NotImplementedError:
            type_ = str
        modelfield = create_response_field(
            name=label.key,
            type_=type_,
        )
        label.__ModelField__ = modelfield
    return modelfield