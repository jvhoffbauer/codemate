    def incr(self, field, value=1):
        return self.__class__.objects.filter(id=self.id).update(
            **{field: F(field) + value}
        )