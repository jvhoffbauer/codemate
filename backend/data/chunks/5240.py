    def all(cls) -> QuerySet[Self] | list[Self]:
        return cls.objects.all()