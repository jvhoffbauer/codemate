    def update_common_attrs(
        self,
        modelfield: ModelField,
        item: Union[FormItem, TableColumn],
        set_default: bool = False,
        is_filter: bool = False,
    ):
        """Set common attributes for FormItem and TableColumn."""
        field_info = modelfield.field_info
        if not is_filter:
            if not PYDANTIC_V2:
                if field_info.max_length:
                    item.maxLength = field_info.max_length
                if field_info.min_length:
                    item.minLength = field_info.min_length
            type_ = annotation_outer_type(modelfield.type_)
            item.required = modelfield.required and not issubclass(type_, bool)
            if set_default and modelfield.default is not Undefined:
                item.value = modelfield.default
        item.name = modelfield.alias
        item.label = (
            _(field_info.title) if field_info.title else _(modelfield.name)
        )  # The use of I18N
        label_name = "labelRemark" if isinstance(item, FormItem) else "remark"
        if getattr(item, label_name, None) is None:
            label = (
                Remark(content=_(field_info.description))
                if field_info.description
                else None
            )  # The use of I18N
            setattr(item, label_name, label)
        return item