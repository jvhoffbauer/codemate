    def get_field_amis_extra(
        self,
        modelfield: ModelField,
        name: str,
    ) -> Union[FormItem, TableColumn, dict]:
        """Get amis extra from pydantic model field.
        You can pass amis configuration through the extra parameter of the pydantic model field.
        """
        extra = field_json_schema_extra(modelfield).get(name, {})
        if not extra:
            return {}
        if callable(extra):
            return extra()
        extra = smart_deepcopy(extra)
        if isinstance(extra, (AmisNode, dict)):
            pass
        elif isinstance(extra, str):
            extra = {"type": extra}
        else:
            extra = {}
        return extra