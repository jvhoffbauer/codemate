    def __eq__(self, other):
        return isinstance(other, EntrypointRoute) and self.path == other.path