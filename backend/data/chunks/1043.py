    def is_sequence_field(field: ModelField) -> bool:
        return field_annotation_is_sequence(field.field_info.annotation)