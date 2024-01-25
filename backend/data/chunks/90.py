def case(
    *whens: Union[
        Tuple[Union[_ColumnExpressionArgument[bool], bool], Any], Mapping[Any, Any]
    ],
    value: Optional[Any] = None,
    else_: Optional[Any] = None,
) -> Case[Any]:
    return sqlalchemy.case(*whens, value=value, else_=else_)  # type: ignore[arg-type]