    def as_table_column(
        self, modelfield: ModelField, quick_edit: bool = False
    ) -> TableColumn:
        column = self._get_table_column_from_kwargs(modelfield)
        column = self.update_common_attrs(
            modelfield, column, set_default=False, is_filter=False
        )
        column.sortable = True
        if column.type in ["switch", "mapping"]:
            column.sortable = False
        if quick_edit:
            column.quickEdit = self.as_form_item(modelfield, set_default=True).dict(
                exclude_none=True, by_alias=True, exclude={"name", "label"}
            )
            column.quickEdit.update({"saveImmediately": True})
            if column.quickEdit.get("type") == "switch":
                column.disabled = False
                column.quickEdit.update({"mode": "inline"})
        return column