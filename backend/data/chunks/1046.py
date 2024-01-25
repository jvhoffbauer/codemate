    def is_bytes_sequence_field(field: ModelField) -> bool:
        return is_bytes_sequence_annotation(field.type_)