@pytest.fixture
def ep(ep_path):
    _shared_counter = 0
    _common_counter = 0

    async def get_shared_counter(
        shared: str = Header("shared"),
    ) -> str:
        nonlocal _shared_counter
        _shared_counter += 1
        yield f"{shared}-{_shared_counter}"

    async def get_common_counter(
        common: str = Body(...),
    ) -> str:
        nonlocal _common_counter
        _common_counter += 1
        yield f"{common}-{_common_counter}"

    ep = jsonrpc.Entrypoint(
        ep_path,
        dependencies=[Depends(get_shared_counter)],
        common_dependencies=[Depends(get_common_counter)],
    )

    @ep.method()
    def probe(
        shared_counter: str = Depends(get_shared_counter),
        common_counter: str = Depends(get_common_counter),
    ) -> Tuple[str, str]:
        return shared_counter, common_counter

    return ep