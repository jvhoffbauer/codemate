    def __getattr__(self, name):
        return getattr(self._redis_client, name)