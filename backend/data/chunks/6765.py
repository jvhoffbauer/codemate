    async def shutdown(self):
        if self.scheduler is not None:
            await self.scheduler.close()