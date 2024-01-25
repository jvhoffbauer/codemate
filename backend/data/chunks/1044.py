    def is_scalar_sequence_field(field: ModelField) -> bool:
        return field_annotation_is_scalar_sequence(field.field_info.annotation)