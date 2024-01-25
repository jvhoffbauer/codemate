    async def get_read_action(self, request: Request) -> Optional[Action]:
        if not self.schema_read:
            return None
        return ActionType.Dialog(
            icon="fas fa-eye",
            tooltip=_("View"),
            dialog=Dialog(
                title=_("View") + " - " + _(self.page_schema.label),
                size=SizeEnum.lg,
                body=await self.get_read_form(request),
            ),
        )