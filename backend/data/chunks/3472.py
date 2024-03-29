def test_openapi_schema():
    client = TestClient(app)
    response = client.get("/openapi.json")
    assert response.status_code == 200, response.text
    assert response.json() == {
        "openapi": "3.1.0",
        "info": {"title": "FastAPI", "version": "0.1.0"},
        "paths": {
            "/users/me": {
                "get": {
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/json": {"schema": {}}},
                        }
                    },
                    "summary": "Read Current User",
                    "operationId": "read_current_user_users_me_get",
                    "security": [{"APIKeyCookie": []}],
                }
            }
        },
        "components": {
            "securitySchemes": {
                "APIKeyCookie": {
                    "type": "apiKey",
                    "name": "key",
                    "in": "cookie",
                    "description": "An API Cookie Key",
                }
            }
        },
    }