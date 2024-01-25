    def get_schema_from_model_field(
        *,
        field: ModelField,
        schema_generator: GenerateJsonSchema,
        model_name_map: ModelNameMap,
        field_mapping: Dict[
            Tuple[ModelField, Literal["validation", "serialization"]], JsonSchemaValue
        ],
        separate_input_output_schemas: bool = True,
    ) -> Dict[str, Any]:
        # This expects that GenerateJsonSchema was already used to generate the definitions
        return field_schema(  # type: ignore[no-any-return]
            field, model_name_map=model_name_map, ref_prefix=REF_PREFIX
        )[0]