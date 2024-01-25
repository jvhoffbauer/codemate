def over(
    element: FunctionElement[_T],
    partition_by: Optional[
        Union[
            Iterable[Union[_ColumnExpressionArgument[Any], Any]],
            _ColumnExpressionArgument[Any],
            Any,
        ]
    ] = None,
    order_by: Optional[
        Union[
            Iterable[Union[_ColumnExpressionArgument[Any], Any]],
            _ColumnExpressionArgument[Any],
            Any,
        ]
    ] = None,
    range_: Optional[Tuple[Optional[int], Optional[int]]] = None,
    rows: Optional[Tuple[Optional[int], Optional[int]]] = None,
) -> Over[_T]:
    return sqlalchemy.over(
        element, partition_by=partition_by, order_by=order_by, range_=range_, rows=rows
    )  # type: ignore[arg-type]