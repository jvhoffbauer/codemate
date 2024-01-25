    async def get_form_item_on_foreign_key(
        self, request: Request, modelfield: ModelField, is_filter: bool = False
    ) -> Union[Service, SchemaNode, None]:
        column = self.parser.get_column(modelfield.alias)
        if column is None:
            return None
        foreign_keys = list(column.foreign_keys) or None
        if foreign_keys is None:
            return None
        admin = self.app.site.get_model_admin(foreign_keys[0].column.table.name)
        if not admin:
            return None
        url = admin.router_path + admin.page_path
        label = modelfield.field_info.title or modelfield.name
        remark = (
            Remark(content=modelfield.field_info.description)
            if modelfield.field_info.description
            else None
        )
        picker = Picker(
            name=modelfield.alias,
            label=label,
            labelField="name",
            valueField="id",
            required=(modelfield.required and not is_filter),
            modalMode="dialog",
            inline=is_filter,
            size="full",
            labelRemark=remark,
            pickerSchema="${body}",
            source="${body.api}",
        )
        return Service(
            name=modelfield.alias,
            schemaApi=AmisAPI(
                method="post",
                url=url,
                data={},
                cache=300000,
                responseData={"controls": [picker]},
            ),
        )