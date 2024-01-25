    @classmethod
    def filter(cls, *args, **kwargs) -> QuerySet[Model]:
        return cls.objects.filter(*args, **kwargs)