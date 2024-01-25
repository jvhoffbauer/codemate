def select(*entities: Any) -> Union[Select, SelectOfScalar]:  # type: ignore
    if len(entities) == 1:
        return SelectOfScalar(*entities)
    return Select(*entities)