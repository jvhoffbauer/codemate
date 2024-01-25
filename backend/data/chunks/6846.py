def test_method_middleware_enter(ep, raw_request):
    @contextlib.asynccontextmanager
    async def middleware(_ctx: JsonRpcContext):
        raise HTTPException(401)
        # noinspection PyUnreachableCode
        yield

    @ep.method(middlewares=[middleware])
    def probe() -> str:
        return "qwe"

    resp = raw_request(
        json_dumps(
            {
                "id": 1,
                "jsonrpc": "2.0",
                "method": "probe",
                "params": {},
            }
        )
    )

    assert resp.status_code == 401
    assert resp.json() == {"detail": "Unauthorized"}