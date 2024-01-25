def create_cloned_field(
    field: ModelField,
    *,
    cloned_types: Optional[MutableMapping[Type[BaseModel], Type[BaseModel]]] = None,
) -> ModelField:
    if PYDANTIC_V2:
        return field
    # cloned_types caches already cloned types to support recursive models and improve
    # performance by avoiding unnecessary cloning
    if cloned_types is None:
        cloned_types = _CLONED_TYPES_CACHE

    original_type = field.type_
    if is_dataclass(original_type) and hasattr(original_type, "__pydantic_model__"):
        original_type = original_type.__pydantic_model__
    use_type = original_type
    if lenient_issubclass(original_type, BaseModel):
        original_type = cast(Type[BaseModel], original_type)
        use_type = cloned_types.get(original_type)
        if use_type is None:
            use_type = create_model(original_type.__name__, __base__=original_type)
            cloned_types[original_type] = use_type
            for f in original_type.__fields__.values():
                use_type.__fields__[f.name] = create_cloned_field(
                    f, cloned_types=cloned_types
                )
    new_field = create_response_field(name=field.name, type_=use_type)
    new_field.has_alias = field.has_alias  # type: ignore[attr-defined]
    new_field.alias = field.alias  # type: ignore[misc]
    new_field.class_validators = field.class_validators  # type: ignore[attr-defined]
    new_field.default = field.default  # type: ignore[misc]
    new_field.required = field.required  # type: ignore[misc]
    new_field.model_config = field.model_config  # type: ignore[attr-defined]
    new_field.field_info = field.field_info
    new_field.allow_none = field.allow_none  # type: ignore[attr-defined]
    new_field.validate_always = field.validate_always  # type: ignore[attr-defined]
    if field.sub_fields:  # type: ignore[attr-defined]
        new_field.sub_fields = [  # type: ignore[attr-defined]
            create_cloned_field(sub_field, cloned_types=cloned_types)
            for sub_field in field.sub_fields  # type: ignore[attr-defined]
        ]
    if field.key_field:  # type: ignore[attr-defined]
        new_field.key_field = create_cloned_field(  # type: ignore[attr-defined]
            field.key_field,  # type: ignore[attr-defined]
            cloned_types=cloned_types,
        )
    new_field.validators = field.validators  # type: ignore[attr-defined]
    new_field.pre_validators = field.pre_validators  # type: ignore[attr-defined]
    new_field.post_validators = field.post_validators  # type: ignore[attr-defined]
    new_field.parse_json = field.parse_json  # type: ignore[attr-defined]
    new_field.shape = field.shape  # type: ignore[attr-defined]
    new_field.populate_validators()  # type: ignore[attr-defined]
    return new_field