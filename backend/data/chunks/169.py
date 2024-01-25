def col(column_expression: _T) -> Mapped[_T]:
    if not isinstance(column_expression, (ColumnClause, Column, InstrumentedAttribute)):
        raise RuntimeError(f"Not a SQLAlchemy column: {column_expression}")
    return column_expression  # type: ignore