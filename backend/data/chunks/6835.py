def test_method(ep, raw_request):
    @ep.method()
    def probe() -> str:
        raise HTTPException(401)

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