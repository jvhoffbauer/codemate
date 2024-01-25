    async def get_list_table_api(self, request: Request) -> AmisAPI:
        api = AmisAPI(
            method="POST",
            url=f"{self.router_path}/list?"
            + "page=${page}&perPage=${perPage}&orderBy=${orderBy}&orderDir=${orderDir}",
            data={"&": "$$"},
        )
        if not await self.has_filter_permission(request, None):
            return api
        for field in self.search_fields:
            alias = self.parser.get_alias(field)
            if alias:
                api.data[alias] = f"[~]${alias}"
        for field in await self.get_list_filter(request):
            if isinstance(field, FormItem):
                api.data[field.name] = f"${field.name}"
            else:
                modelfield = self.parser.get_modelfield(field)
                if modelfield and issubclass(
                    modelfield.type_, (datetime.datetime, datetime.date, datetime.time)
                ):
                    api.data[modelfield.alias] = f"[-]${modelfield.alias}"
        return api