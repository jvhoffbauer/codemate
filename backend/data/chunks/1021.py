        @property
        def alias(self) -> str:
            a = self.field_info.alias
            return a if a is not None else self.name