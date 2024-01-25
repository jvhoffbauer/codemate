    def is_pv1_scalar_sequence_field(field: ModelField) -> bool:
        if (field.shape in sequence_shapes) and not lenient_issubclass(  # type: ignore[attr-defined]
            field.type_, BaseModel
        ):
            if field.sub_fields is not None:  # type: ignore[attr-defined]
                for sub_field in field.sub_fields:  # type: ignore[attr-defined]
                    if not is_pv1_scalar_field(sub_field):
                        return False
            return True
        if _annotation_is_sequence(field.type_):
            return True
        return False