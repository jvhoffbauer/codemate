def ep(ep_path):
    ep = Entrypoint(
        ep_path,
        dependencies=[Depends(auth_user)],
    )

    @ep.method()
    def probe() -> str:
        return "ok"

    return ep