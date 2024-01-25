    def create_model_by_fields(
        name: str,
        fields: Sequence[ModelField],
        *,
        set_none: bool = False,
        extra: str = "ignore",
        **kwargs,
    ) -> Type[BaseModel]:
        __config__ = marge_model_config(
            AllowExtraModelMixin, {"extra": extra, **kwargs}
        )
        __validators__ = None
        if set_none:
            __validators__ = {
                "root_validator_skip_blank": root_validator(pre=True, allow_reuse=True)(
                    root_validator_skip_blank
                )
            }
            for f in fields:
                f.required = False
                f.allow_none = True
        model = create_model(name, __config__=__config__, __validators__=__validators__)  # type: ignore
        model.__fields__ = {f.name: f for f in fields}
        return model