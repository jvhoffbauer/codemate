    def set_fields_set(
        new_object: InstanceOrType["SQLModel"], fields: Set["FieldInfo"]
    ) -> None:
        object.__setattr__(new_object, "__pydantic_fields_set__", fields)