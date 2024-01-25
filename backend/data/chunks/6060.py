    async def get_update_action(
        self, request: Request, bulk: bool = False
    ) -> Optional[Action]:
        if not bulk:
            return ActionType.Dialog(
                icon="fa fa-pencil",
                tooltip=_("Update"),
                dialog=Dialog(
                    title=_("Update") + " - " + _(self.page_schema.label),
                    size=SizeEnum.lg,
                    body=await self.get_update_form(request, bulk=bulk),
                ),
            )
        elif self.bulk_update_fields:
            return ActionType.Dialog(
                label=_("Bulk Update"),
                dialog=Dialog(
                    title=_("Bulk Update") + " - " + _(self.page_schema.label),
                    size=SizeEnum.lg,
                    body=await self.get_update_form(request, bulk=True),
                ),
            )
        else:
            return None