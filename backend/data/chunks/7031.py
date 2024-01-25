def test_basic(ep, app, app_client):
    @ep.method()
    def probe(
        data: List[str] = Body(..., examples=["111", "222"]),
        amount: int = Body(..., gt=5, examples=[10]),
    ) -> List[int]:
        del data, amount
        return [1, 2, 3]

    app.bind_entrypoint(ep)

    resp = app_client.get("/openrpc.json")

    assert resp.json()["methods"] == [
        {
            "name": "probe",
            "params": [
                {
                    "name": "data",
                    "schema": {
                        "title": "Data",
                        "examples": ["111", "222"],
                        "type": "array",
                        "items": {"type": "string"},
                    },
                    "required": True,
                },
                {
                    "name": "amount",
                    "schema": {
                        "title": "Amount",
                        "exclusiveMinimum": 5,
                        "examples": [10],
                        "type": "integer",
                    },
                    "required": True,
                },
            ],
            "result": {
                "name": "probe_Result",
                "schema": {
                    "title": "Result",
                    "type": "array",
                    "items": {"type": "integer"},
                },
            },
            "tags": [],
            "errors": [],
        }
    ]