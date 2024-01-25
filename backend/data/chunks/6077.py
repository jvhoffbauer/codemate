    async def get_action(self, request: Request, **kwargs) -> Action:
        action = (
            self.action
            and self.action.copy()
            or ActionType.Dialog(label=_("Custom form actions"), dialog=Dialog())
        )
        node: AmisNode = getattr(action, action.actionType, None)
        if node:
            node.title = (
                node.title or action.label or action.tooltip
            )  # only override if not set
            node.size = node.size or SizeEnum.xl
            node.body = Service(
                schemaApi=AmisAPI(
                    method="post",
                    url=self.router_path + self.page_path,
                    responseData={
                        "&": "${body}",
                        "submitText": "",
                    },
                )
            )
        return action