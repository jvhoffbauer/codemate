    @classmethod
    def create(cls, **kwargs) -> Self:
        return cls.objects.create(**kwargs)