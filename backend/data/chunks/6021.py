    async def get_action(self, request: Request, name: str) -> Action:
        admin_action = self.registered_admin_actions.get(name)
        return await admin_action.get_action(request)