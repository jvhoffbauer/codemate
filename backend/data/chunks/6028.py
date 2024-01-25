    async def get_form(self, request: Request) -> Form:
        form = self.form or Form()
        form.api = AmisAPI(method="POST", url=f"{self.router_path}{self.form_path}")
        form.initApi = (
            AmisAPI(method="GET", url=f"{self.router_path}{self.form_path}")
            if self.form_init
            else None
        )
        form.title = ""
        actions = await self.get_actions(request, flag="item")
        if actions:
            form.actions = actions
        form.body = []
        for modelfield in model_fields(self.schema).values():
            formitem = await self.get_form_item(request, modelfield)
            if formitem:
                form.body.append(formitem)
        return form