def ep(ep_path):
    _shared_counter = 0
    _common_counter = 0

    def get_shared_counter(
        shared: str = Header("shared"),
    ) -> str:
        nonlocal _shared_counter
        _shared_counter += 1
        return f"{shared}-{_shared_counter}"

    def get_common_counter(
        common: str = Body(...),
    ) -> Tuple[str, int]:
        nonlocal _common_counter
        _common_counter += 1
        return common, _common_counter

    ep = jsonrpc.Entrypoint(
        ep_path,
        dependencies=[Depends(get_shared_counter)],
        common_dependencies=[Depends(get_common_counter)],
    )

    @ep.method()
    def probe(
        shared_counter: str = Depends(get_shared_counter),
        common_counter: Tuple[str, int] = Depends(get_common_counter),
    ) -> Tuple[str, str, int]:
        return shared_counter, common_counter[0], common_counter[1]

    return ep