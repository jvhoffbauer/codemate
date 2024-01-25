    def __getattr__(self, name):
        return getattr(self._schedule, name)