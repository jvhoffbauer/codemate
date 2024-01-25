    async def get_select(self, request: Request) -> Select:
        return select(*self._select_entities.values())