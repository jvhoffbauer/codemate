    def get_field_metadata(field: Any) -> Any:
        metadata = FakeMetadata()
        metadata.max_length = field.field_info.max_length
        metadata.max_digits = getattr(field.type_, "max_digits", None)
        metadata.decimal_places = getattr(field.type_, "decimal_places", None)
        return metadata