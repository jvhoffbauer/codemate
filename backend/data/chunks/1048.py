    def serialize_sequence_value(*, field: ModelField, value: Any) -> Sequence[Any]:
        origin_type = (
            get_origin(field.field_info.annotation) or field.field_info.annotation
        )
        assert issubclass(origin_type, sequence_types)  # type: ignore[arg-type]
        return sequence_annotation_to_type[origin_type](value)  # type: ignore[no-any-return]