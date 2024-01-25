    def get_modelfield(
        self, field: Union[ModelField, SqlaInsAttr, Label], clone: bool = False
    ) -> Optional[ModelFieldType]:
        """Get pydantic ModelField from sqlmodel field.
        Args:
            field:  ModelField, SQLModelField or Label
            clone:  Whether to return a cloned of the original ModelField.

        Returns:  pydantic ModelField or ModelFieldProxy.
        """
        modelfield = None
        update = {}
        if isinstance(field, InstrumentedAttribute):
            modelfield = self.get_table_model_fields(field.class_).get(field.key, None)
            if not modelfield:  # Maybe it's a declared_attr or column_property.
                return None
            if field.class_.__table__ is not self.__table__:
                update = {
                    "name": self.get_name(field),
                    "alias": self.get_alias(field),
                }
        elif isinstance(field, str) and field in self.__fields__:
            modelfield = self.__fields__[field]
        elif isinstance(field, ModelField):
            modelfield = field
        elif isinstance(field, Label):
            modelfield = _get_label_modelfield(field)
        if not modelfield:
            return None
        field_proxy = ModelFieldProxy(modelfield, update=update)
        return field_proxy.cloned_field() if clone else field_proxy