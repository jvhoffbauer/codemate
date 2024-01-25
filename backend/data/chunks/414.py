        @field_validator("name", "secret_name", "age")
        def reject_none(cls, v):
            assert v is not None
            return v