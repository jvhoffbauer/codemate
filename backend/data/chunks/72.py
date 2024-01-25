    def post_init_field_info(field_info: FieldInfo) -> None:
        field_info._validate()  # type: ignore[attr-defined]