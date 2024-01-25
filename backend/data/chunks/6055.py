    async def get_create_form(self, request: Request, bulk: bool = False) -> Form:
        fields = [
            field
            for field in model_fields(self.schema_create).values()
            if field.name != self.pk_name
        ]
        if not bulk:
            return Form(
                api=f"post:{self.router_path}/item",
                name=CrudEnum.create,
                body=await self._conv_modelfields_to_formitems(
                    request, fields, CrudEnum.create
                ),
            )
        columns, keys = [], {}
        for field in fields:
            column = await self.get_list_column(
                request, self.parser.get_modelfield(field)
            )
            keys[column.name] = "${" + column.label + "}"
            column.name = column.label
            columns.append(column)
        return Form(
            api=AmisAPI(
                method="post",
                url=f"{self.router_path}/item",
                data={"&": {"$excel": keys}},
            ),
            name=CrudEnum.create,
            mode=DisplayModeEnum.normal,
            body=[
                InputExcel(name="excel"),
                InputTable(
                    name="excel",
                    showIndex=True,
                    columns=columns,
                    addable=True,
                    copyable=True,
                    editable=True,
                    removable=True,
                ),
            ],
        )