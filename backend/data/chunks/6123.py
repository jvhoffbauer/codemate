def get_model_label_field_name(model: Type[BaseModel]) -> str:
    """Get model label field name. The label field is used to display the model name in the form."""
    label_field_name = model_config_attr(model, "label_field_name", None)
    if label_field_name:
        return label_field_name
    for filed in model_fields(model).values():
        if filed.alias in ["name", "title", "label"]:
            return filed.alias
    return "id"