    def _get_table_column_from_kwargs(self, modelfield: ModelField) -> TableColumn:
        table_column = self.get_field_amis_extra(modelfield, "amis_table_column")
        if isinstance(table_column, TableColumn):
            return table_column
        kwargs = self.get_field_amis_table_column_type(modelfield.type_)
        return TableColumn(**kwargs).update_from_dict(table_column)