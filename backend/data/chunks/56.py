    def get_field_metadata(field: Any) -> Any:
        for meta in field.metadata:
            if isinstance(meta, PydanticMetadata):
                return meta
        return FakeMetadata()