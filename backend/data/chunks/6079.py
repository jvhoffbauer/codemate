    async def get_action(self, request: Request, **kwargs) -> Action:
        action = await super().get_action(request, **kwargs)
        node: AmisNode = getattr(action, action.actionType, None)
        if node:
            node.body = Service(
                schemaApi=AmisAPI(
                    method="post",
                    url=self.router_path
                    + self.page_path
                    + "?item_id=${IF(ids, ids, id)}",
                    responseData={
                        "&": "${body}",
                        "api.url": "${body.api.url}?item_id=${api.query.item_id}",
                        "initApi.url": "${body.initApi.url}?item_id=${api.query.item_id}"
                        if self.form_init
                        else None,
                        "submitText": "",
                    },
                )
            )
        return action