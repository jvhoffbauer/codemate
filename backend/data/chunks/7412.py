    def __setitem__(self, name, value):
        self._redis_client[name] = value