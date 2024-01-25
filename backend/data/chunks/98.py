def label(
    name: str,
    element: Union[_ColumnExpressionArgument[_T], _T],
    type_: Optional["_TypeEngineArgument[_T]"] = None,
) -> Label[_T]:
    return sqlalchemy.label(name, element, type_=type_)  # type: ignore[arg-type]