    def is_scalar_field(field: ModelField) -> bool:
        from fastapi import params

        return field_annotation_is_scalar(
            field.field_info.annotation
        ) and not isinstance(field.field_info, params.Body)