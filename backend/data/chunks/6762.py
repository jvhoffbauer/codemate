    def __eq__(self, other):
        return isinstance(other, Entrypoint) and self.routes == other.routes