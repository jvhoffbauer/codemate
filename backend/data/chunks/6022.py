    async def get_actions(self, request: Request, flag: str) -> List[Action]:
        actions = []
        for admin_action in self.registered_admin_actions.values():
            if flag not in admin_action.flags:
                continue
            if await self.has_action_permission(request, name=admin_action.name):
                actions.append(
                    await admin_action.get_action(request, name=admin_action.name)
                )
        return list(filter(None, actions))