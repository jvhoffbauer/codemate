    def __iter__(self) -> Iterator[PageSchemaAdminT]:
        return self._children.__iter__()