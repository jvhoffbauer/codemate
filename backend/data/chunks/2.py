    def __eq__(self, o: object) -> bool:
        return isinstance(o, _DefaultPlaceholder) and o.value == self.value