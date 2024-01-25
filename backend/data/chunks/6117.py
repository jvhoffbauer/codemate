    def _get_form_item_from_kwargs(
        self, modelfield: ModelField, is_filter: bool = False
    ) -> FormItem:
        formitem = self.get_field_amis_extra(
            modelfield, ["amis_form_item", "amis_filter_item"][is_filter]
        )
        # List type parse to InputArray
        outer_type = field_outer_type(modelfield) or modelfield.type_
        if field_annotation_is_sequence(outer_type):
            if not isinstance(formitem, FormItem):
                formitem = InputArray(**formitem)
            elif not isinstance(formitem, InputArray):
                return formitem
            # Parse the internal type of the list.
            type_ = scalar_sequence_inner_type(outer_type)
            kwargs = self.get_field_amis_form_item_type(
                type_=type_, is_filter=is_filter
            )
            update = formitem.items.amis_dict() if formitem.items else {}
            if update:
                kwargs = deep_update(kwargs, update)
            formitem.items = FormItem(**kwargs)
        if isinstance(formitem, FormItem):
            return formitem
        # other type parse to FormItem
        kwargs = self.get_field_amis_form_item_type(
            type_=modelfield.type_,
            is_filter=is_filter,
            required=modelfield.required and not field_allow_none(modelfield),
        )
        return FormItem(**kwargs).update_from_dict(formitem)