def collate(
    expression: Union[_ColumnExpressionArgument[str], str], collation: str
) -> BinaryExpression[str]:
    return sqlalchemy.collate(expression, collation)  # type: ignore[arg-type]