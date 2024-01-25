    def is_field_noneable(field: "FieldInfo") -> bool:
        if not field.required:  # type: ignore[attr-defined]
            # Taken from [Pydantic](https://github.com/samuelcolvin/pydantic/blob/v1.8.2/pydantic/fields.py#L946-L947)
            return field.allow_none and (  # type: ignore[attr-defined]
                field.shape != SHAPE_SINGLETON or not field.sub_fields  # type: ignore[attr-defined]
            )
        return field.allow_none  # type: ignore[no-any-return, attr-defined]