    def is_bytes_field(field: ModelField) -> bool:
        return lenient_issubclass(field.type_, bytes)