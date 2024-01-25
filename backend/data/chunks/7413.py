    def __delitem__(self, name):
        del self._redis_client[name]