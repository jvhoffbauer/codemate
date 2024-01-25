    def __init__(
        self,
        *,
        name: str,
        type_: Type[Any],
        required: bool = False,
        field_info: Optional[FieldInfo] = None,
        **kwargs: Any,
    ) -> None:
        if PYDANTIC_V2:
            field_info = field_info or FieldInfo(default=None)
            field_info.annotation = type_
        else:
            kwargs.setdefault("type_", type_)
            kwargs.setdefault("required", required)
            kwargs.setdefault("class_validators", {})
            kwargs.setdefault("model_config", BaseConfig)
        super().__init__(name=name, field_info=field_info, **kwargs)