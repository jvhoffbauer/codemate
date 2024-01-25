    def get_type_from_field(field: Any) -> Any:
        type_: Any = field.annotation
        # Resolve Optional fields
        if type_ is None:
            raise ValueError("Missing field type")
        origin = get_origin(type_)
        if origin is None:
            return type_
        if _is_union_type(origin):
            bases = get_args(type_)
            if len(bases) > 2:
                raise ValueError(
                    "Cannot have a (non-optional) union as a SQLAlchemy field"
                )
            # Non optional unions are not allowed
            if bases[0] is not NoneType and bases[1] is not NoneType:
                raise ValueError(
                    "Cannot have a (non-optional) union as a SQLlchemy field"
                )
            # Optional unions are allowed
            return bases[0] if bases[0] is not NoneType else bases[1]
        return origin