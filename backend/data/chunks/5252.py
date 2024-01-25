    def one_or_404(cls, **kwargs) -> Self:
        return get_object_or_404(cls.objects.filter(**kwargs))