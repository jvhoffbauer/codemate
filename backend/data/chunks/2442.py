def test_openapi_schema():
    response = client.get("/openapi.json")
    assert response.status_code == 200, response.text
    assert response.json() == {
        "openapi": "3.1.0",
        "info": {"title": "FastAPI", "version": "0.1.0"},
        "paths": {
            "/items/": {
                "get": {
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/json": {"schema": {}}},
                        }
                    },
                    "summary": "Read Items",
                    "operationId": "read_items_items__get",
                    "security": [{"OAuth2AuthorizationCodeBearer": []}],
                }
            }
        },
        "components": {
            "securitySchemes": {
                "OAuth2AuthorizationCodeBearer": {
                    "type": "oauth2",
                    "flows": {
                        "authorizationCode": {
                            "authorizationUrl": "authorize",
                            "tokenUrl": "token",
                            "scopes": {},
                        }
                    },
                    "description": "OAuth2 Code Bearer",
                }
            }
        },
    }