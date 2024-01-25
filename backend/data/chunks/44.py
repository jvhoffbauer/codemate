def _is_union_type(t: Any) -> bool:
    return t is UnionType or t is Union