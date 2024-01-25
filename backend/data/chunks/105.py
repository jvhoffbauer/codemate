def within_group(
    element: FunctionElement[_T], *order_by: Union[_ColumnExpressionArgument[Any], Any]
) -> WithinGroup[_T]:
    return sqlalchemy.within_group(element, *order_by)  # type: ignore[arg-type]