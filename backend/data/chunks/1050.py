    def create_body_model(
        *, fields: Sequence[ModelField], model_name: str
    ) -> Type[BaseModel]:
        field_params = {f.name: (f.field_info.annotation, f.field_info) for f in fields}
        BodyModel: Type[BaseModel] = create_model(model_name, **field_params)  # type: ignore[call-overload]
        return BodyModel