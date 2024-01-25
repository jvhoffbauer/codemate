    def schema_name_prefix(self):
        if self.__class__ is SqlalchemyCrud:
            return self.model.__name__
        return super().schema_name_prefix