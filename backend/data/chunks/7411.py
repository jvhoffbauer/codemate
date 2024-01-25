    def __getitem__(self, name):
        return self._redis_client[name]