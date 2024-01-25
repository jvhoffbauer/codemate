    async def get_update_form(self, request: Request, bulk: bool = False) -> Form:
        extra = {}
        if not bulk:
            api = f"put:{self.router_path}/item/${self.pk_name}"
            fields = model_fields(self.schema_update).values()
            if self.schema_read:
                extra["initApi"] = f"get:{self.router_path}/item/${self.pk_name}"
        else:
            api = f"put:{self.router_path}/item/" + "${ids|raw}"
            fields = self.bulk_update_fields
        return Form(
            api=api,
            name=CrudEnum.update,
            body=await self._conv_modelfields_to_formitems(
                request, fields, CrudEnum.update
            ),
            submitText=None,
            trimValues=True,
            **extra,
        )