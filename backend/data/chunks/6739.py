    def __eq__(self, other):
        return (
            isinstance(other, MethodRoute)
            and self.path == other.path
            and self.func == other.func
        )