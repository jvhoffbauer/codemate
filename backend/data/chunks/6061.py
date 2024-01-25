    async def _conv_modelfields_to_formitems(
        self,
        request: Request,
        fields: Iterable[Union[SqlaField, ModelField, FormItem]],
        action: CrudEnum = None,
    ) -> List[FormItem]:
        items = []
        for field in fields:
            if isinstance(field, FormItem):
                items.append(field)
            else:
                field = self.parser.get_modelfield(field)
                if field:
                    item = await self.get_form_item(request, field, action)
                    if item:
                        items.append(item)
        items.sort(key=lambda i: isinstance(i, Service))
        return items