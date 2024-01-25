    def field_allow_none(field: ModelField) -> bool:
        if is_union(field.field_info.annotation):
            for t in get_args(field.field_info.annotation):
                if is_none_type(t):
                    return True
        return False