    def _model_rebuild(model: Type[BaseModel]) -> None:
        model.update_forward_refs()