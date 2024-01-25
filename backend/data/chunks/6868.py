def ep(ep_path):
    ep = jsonrpc.Entrypoint(
        ep_path,
        dependencies=[Depends(get_auth_token)],
        common_dependencies=[Depends(get_common_dep)],
    )

    @ep.method()
    def probe(
        data: List[str] = Body(..., examples=["111", "222"]),
    ) -> List[int]:
        del data
        return [1, 2, 3]

    def get_probe2_dep(
        probe2_dep: int = Body(...),
    ) -> int:
        return probe2_dep

    @ep.method()
    def probe2(
        auth_token: str = Depends(get_auth_token),
        probe2_dep: int = Depends(get_probe2_dep),
    ) -> int:
        del auth_token
        del probe2_dep
        return 1

    return ep