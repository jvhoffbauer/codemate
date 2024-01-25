    def copy_field_info(*, field_info: FieldInfo, annotation: Any) -> FieldInfo:
        return type(field_info).from_annotation(annotation)