    async def get_create_action(
        self, request: Request, bulk: bool = False
    ) -> Optional[Action]:
        if not bulk:
            return ActionType.Dialog(
                icon="fa fa-plus pull-left",
                label=_("Create"),
                level=LevelEnum.primary,
                dialog=Dialog(
                    title=_("Create") + " - " + _(self.page_schema.label),
                    size=SizeEnum.lg,
                    body=await self.get_create_form(request, bulk=bulk),
                ),
            )
        return ActionType.Dialog(
            icon="fa fa-plus pull-left",
            label=_("Bulk Create"),
            level=LevelEnum.primary,
            dialog=Dialog(
                title=_("Bulk Create") + " - " + _(self.page_schema.label),
                size=SizeEnum.full,
                body=await self.get_create_form(request, bulk=bulk),
            ),
        )