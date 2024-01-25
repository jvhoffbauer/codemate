    async def get_read_form(self, request: Request) -> Form:
        return Form(
            initApi=f"get:{self.router_path}/item/${self.pk_name}",
            name=CrudEnum.read,
            body=await self._conv_modelfields_to_formitems(
                request, model_fields(self.schema_read).values(), CrudEnum.read
            ),
            submitText=None,
            static=True,
            disabled=True,
        )