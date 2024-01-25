    def field_json_schema_extra(field: ModelField) -> Dict[str, Any]:
        return field.field_info.extra or {}