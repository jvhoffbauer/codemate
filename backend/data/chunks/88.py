def between(
    expr: Union[_ColumnExpressionOrLiteralArgument[_T], _T],
    lower_bound: Any,
    upper_bound: Any,
    symmetric: bool = False,
) -> BinaryExpression[bool]:
    return sqlalchemy.between(expr, lower_bound, upper_bound, symmetric=symmetric)  # type: ignore[arg-type]