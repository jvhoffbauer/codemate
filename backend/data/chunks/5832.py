def LabelField(label: Label, field: FieldInfo, type_: type = str) -> Label:
    """Use for adding FieldInfo to sqlalchemy Label type"""
    modelfield = _get_label_modelfield(label)
    field.alias = label.key
    if PYDANTIC_V2:
        field.annotation = type_
    modelfield.field_info = field
    label.__ModelField__ = modelfield
    return label