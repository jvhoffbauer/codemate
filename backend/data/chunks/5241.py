    @classmethod
    def get(cls, pk) -> Self:
        return cls.objects.get(pk=pk)