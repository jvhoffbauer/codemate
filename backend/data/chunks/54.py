    def is_field_noneable(field: "FieldInfo") -> bool:
        if getattr(field, "nullable", Undefined) is not Undefined:
            return field.nullable  # type: ignore
        origin = get_origin(field.annotation)
        if origin is not None and _is_union_type(origin):
            args = get_args(field.annotation)
            if any(arg is NoneType for arg in args):
                return True
        if not field.is_required():
            if field.default is Undefined:
                return False
            if field.annotation is None or field.annotation is NoneType:  # type: ignore[comparison-overlap]
                return True
            return False
        return False