    def serialize_sequence_value(*, field: ModelField, value: Any) -> Sequence[Any]:
        return sequence_shape_to_type[field.shape](value)  # type: ignore[no-any-return,attr-defined]