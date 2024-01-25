def test_openapi_schema():
    response = client.get("/openapi.json")
    assert response.status_code == 200, response.text
    assert response.json() == {
        "openapi": "3.1.0",
        "info": {"title": "FastAPI", "version": "0.1.0"},
        "paths": {
            "/pydantic": {
                "get": {
                    "summary": "Redirect Pydantic",
                    "operationId": "redirect_pydantic_pydantic_get",
                    "responses": {"302": {"description": "Successful Response"}},
                }
            }
        },
    }