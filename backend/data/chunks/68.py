    def get_relationship_to(
        name: str,
        rel_info: "RelationshipInfo",
        annotation: Any,
    ) -> Any:
        temp_field = ModelField.infer(  # type: ignore[attr-defined]
            name=name,
            value=rel_info,
            annotation=annotation,
            class_validators=None,
            config=SQLModelConfig,
        )
        relationship_to = temp_field.type_
        if isinstance(temp_field.type_, ForwardRef):
            relationship_to = temp_field.type_.__forward_arg__
        return relationship_to