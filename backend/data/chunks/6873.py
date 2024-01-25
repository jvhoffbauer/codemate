    def probe2(
        auth_token: str = Depends(get_auth_token),
        probe2_dep: int = Depends(get_probe2_dep),
    ) -> int:
        del auth_token
        del probe2_dep
        return 1