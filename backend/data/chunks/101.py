def or_(  # type: ignore[empty-body]
    initial_clause: Union[Literal[False], _ColumnExpressionArgument[bool], bool],
    *clauses: Union[_ColumnExpressionArgument[bool], bool],
) -> ColumnElement[bool]:
    return sqlalchemy.or_(initial_clause, *clauses)  # type: ignore[arg-type]