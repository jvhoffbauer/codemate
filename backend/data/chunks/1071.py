    def create_body_model(
        *, fields: Sequence[ModelField], model_name: str
    ) -> Type[BaseModel]:
        BodyModel = create_model(model_name)
        for f in fields:
            BodyModel.__fields__[f.name] = f  # type: ignore[index]
        return BodyModel