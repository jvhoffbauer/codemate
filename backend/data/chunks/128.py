@overload
def select(  # type: ignore
    entity_0: _TScalar_0,
    __ent1: _TCCA[_T1],
    __ent2: _TCCA[_T2],
) -> Select[Tuple[_TScalar_0, _T1, _T2]]:
    ...