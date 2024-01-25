    def is_pv1_scalar_field(field: ModelField) -> bool:
        from fastapi import params

        field_info = field.field_info
        if not (
            field.shape == SHAPE_SINGLETON  # type: ignore[attr-defined]
            and not lenient_issubclass(field.type_, BaseModel)
            and not lenient_issubclass(field.type_, dict)
            and not field_annotation_is_sequence(field.type_)
            and not is_dataclass(field.type_)
            and not isinstance(field_info, params.Body)
        ):
            return False
        if field.sub_fields:  # type: ignore[attr-defined]
            if not all(
                is_pv1_scalar_field(f)
                for f in field.sub_fields  # type: ignore[attr-defined]
            ):
                return False
        return True