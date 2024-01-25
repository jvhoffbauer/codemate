def field_annotation_is_sequence(annotation: Union[Type[Any], None]) -> bool:
    return _annotation_is_sequence(annotation) or _annotation_is_sequence(
        get_origin(annotation)
    )