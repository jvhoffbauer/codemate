    async def _get_list_columns_for_actions(self, request) -> List[ColumnOperation]:
        columns = []
        actions = await self.get_actions(request, flag="column") or []
        action_names = {action.name for action in actions}
        if self.display_item_action_as_column:
            item_actions = await self.get_actions(request, flag="item") or []
            actions.extend(
                action for action in item_actions if action.name not in action_names
            )
        if actions:
            columns.append(
                ColumnOperation(
                    fixed="right",
                    label=_("Operation"),
                    buttons=actions,
                )
            )
        return columns