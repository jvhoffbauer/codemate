def parser_item_id(
    item_id: str = Path(
        ...,
        min_length=1,
        title="pk",
        examples=["1", "1,2,3"],
        description="Primary key or list of primary keys",
    )
) -> List[str]:
    """Deprecated, use ItemIdListDepend and parser_str_set_list instead"""
    warnings.warn(
        "Deprecated, use ItemIdListDepend and parser_str_set_list instead",
        DeprecationWarning,
        stacklevel=2,
    )
    return parser_str_set_list(item_id)