def tuple_(
    *clauses: Union[_ColumnExpressionArgument[Any], Any],
    types: Optional[Sequence["_TypeEngineArgument[Any]"]] = None,
) -> Tuple[Any, ...]:
    return sqlalchemy.tuple_(*clauses, types=types)  # type: ignore[return-value]