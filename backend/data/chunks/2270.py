def get_query_type_frozenset(query: FrozenSet[int] = Query(...)):
    return ",".join(map(str, sorted(query)))