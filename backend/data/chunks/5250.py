    def find_first(cls, order_by: Optional[list[str]] = None, **kwargs) -> Self | None:
        if not order_by:
            order_by = ["-id"]
        return cls.objects.filter(**kwargs).order_by(*order_by).first()