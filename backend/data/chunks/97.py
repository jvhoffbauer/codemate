def funcfilter(
    func: FunctionElement[_T], *criterion: Union[_ColumnExpressionArgument[bool], bool]
) -> FunctionFilter[_T]:
    return sqlalchemy.funcfilter(func, *criterion)  # type: ignore[arg-type]