    @validator("url", always=True)
    def build_url(cls, v: Any, field: Field, values: dict):
        if isinstance(v, URL):
            return v
        args = {k: str(v) for k, v in values.items() if v is not None}
        return URL(**args)