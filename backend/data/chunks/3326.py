        def lower_username(cls, name: str, info: ValidationInfo):
            if not name.endswith("A"):
                raise ValueError("name must end in A")
            return name