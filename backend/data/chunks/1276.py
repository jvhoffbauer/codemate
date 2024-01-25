    def __getattr__(self, name):
        return self._state.get()[name]