    async def get_form_item(
        self, request: Request, modelfield: ModelField, action: CrudEnum
    ) -> Union[FormItem, SchemaNode, None]:
        is_filter = True if action in [CrudEnum.filter, CrudEnum.list] else False
        set_default = action == CrudEnum.create
        return await self.get_form_item_on_foreign_key(
            request, modelfield, is_filter=is_filter
        ) or self.amis_parser.as_form_item(
            modelfield, is_filter=is_filter, set_default=set_default
        )