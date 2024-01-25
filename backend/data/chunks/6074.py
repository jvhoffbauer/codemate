    async def get_action(self, request: Request, **kwargs) -> Action:
        if not self.getter:
            return self.action
        action = self.getter(request)
        if asyncio.iscoroutine(action):
            action = await action
        return action