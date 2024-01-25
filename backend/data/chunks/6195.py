    def create_model_by_fields(
        name: str,
        fields: Sequence[ModelField],
        *,
        set_none: bool = False,
        extra: str = "ignore",
        **kwargs,
    ) -> Type[BaseModel]:
        if kwargs.pop("orm_mode", False):
            kwargs.setdefault("from_attributes", True)
        __config__ = marge_model_config(
            AllowExtraModelMixin, {"extra": extra, **kwargs}
        )
        __validators__ = None

        if set_none:
            __validators__ = {
                "root_validator_skip_blank": model_validator(mode="before")(
                    root_validator_skip_blank
                )
            }
            for f in fields:
                f.field_info.annotation = Optional[f.field_info.annotation]
                f.field_info.default = None
        field_params = {f.name: (f.field_info.annotation, f.field_info) for f in fields}
        model: Type[BaseModel] = create_model(
            name, __config__=__config__, __validators__=__validators__, **field_params
        )
        return model