    def __setattr__(self, name, value):
        self._state.get()[name] = value