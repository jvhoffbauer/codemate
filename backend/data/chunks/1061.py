    def get_compat_model_name_map(fields: List[ModelField]) -> ModelNameMap:
        models = get_flat_models_from_fields(fields, known_models=set())
        return get_model_name_map(models)  # type: ignore[no-any-return]