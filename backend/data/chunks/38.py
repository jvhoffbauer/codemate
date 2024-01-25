    @classmethod
    @deprecated(
        """
        🚨 `obj.parse_obj(data)` was deprecated in SQLModel 0.0.14, you should
        instead use `obj.model_validate(data)`.
        """
    )
    def parse_obj(
        cls: Type[_TSQLModel], obj: Any, update: Optional[Dict[str, Any]] = None
    ) -> _TSQLModel:
        if not IS_PYDANTIC_V2:
            obj = cls._enforce_dict_if_root(obj)  # type: ignore[attr-defined] # noqa
        return cls.model_validate(obj, update=update)