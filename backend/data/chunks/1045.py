    def is_bytes_field(field: ModelField) -> bool:
        return is_bytes_or_nonable_bytes_annotation(field.type_)