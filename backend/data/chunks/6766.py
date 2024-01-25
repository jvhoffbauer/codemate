    async def get_scheduler(self):
        if self.scheduler is not None:
            return self.scheduler
        self.scheduler = self.scheduler_factory(**(self.scheduler_kwargs or {}))
        return self.scheduler