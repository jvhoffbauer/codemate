    def __eq__(self, other):
        if not isinstance(other, User):
            return False
        return self.name == other.name