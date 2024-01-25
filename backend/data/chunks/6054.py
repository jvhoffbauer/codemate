    async def get_list_filter_form(self, request: Request) -> Form:
        body = await self._conv_modelfields_to_formitems(
            request, await self.get_list_filter(request), CrudEnum.filter
        )
        return Form(
            type="",
            title=_("Filter"),
            name=CrudEnum.filter,
            body=body,
            mode=DisplayModeEnum.inline,
            actions=[
                Action(
                    actionType="clear-and-submit",
                    label=_("Clear"),
                    level=LevelEnum.default,
                ),
                Action(
                    actionType="reset-and-submit",
                    label=_("Reset"),
                    level=LevelEnum.default,
                ),
                Action(actionType="submit", label=_("Search"), level=LevelEnum.primary),
            ],
            trimValues=True,
        )