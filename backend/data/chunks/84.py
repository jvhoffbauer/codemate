def and_(
    initial_clause: Union[Literal[True], _ColumnExpressionArgument[bool], bool],
    *clauses: Union[_ColumnExpressionArgument[bool], bool],
) -> ColumnElement[bool]:
    return sqlalchemy.and_(initial_clause, *clauses)  # type: ignore[arg-type]