    def _get_model_config(model: BaseModel) -> Any:
        return model.__config__  # type: ignore[attr-defined]