def test_openapi_schema():
    response = client.get("/openapi.json")
    assert response.status_code == 200, response.text
    assert response.json() == {
        "openapi": "3.1.0",
        "info": {"title": "FastAPI", "version": "0.1.0"},
        "paths": {
            "/fastapi": {
                "get": {
                    "summary": "Redirect Fastapi",
                    "operationId": "redirect_fastapi_fastapi_get",
                    "responses": {"307": {"description": "Successful Response"}},
                }
            }
        },
    }