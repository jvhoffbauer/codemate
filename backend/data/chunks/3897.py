def test_openapi_schema(client: TestClient):
    response = client.get("/openapi.json")
    assert response.status_code == 200, response.text
    assert response.json() == {
        "openapi": "3.1.0",
        "info": {"title": "FastAPI", "version": "0.1.0"},
        "paths": {
            "/keyword-weights/": {
                "get": {
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "title": "Response Read Keyword Weights Keyword Weights  Get",
                                        "type": "object",
                                        "additionalProperties": {"type": "number"},
                                    }
                                }
                            },
                        }
                    },
                    "summary": "Read Keyword Weights",
                    "operationId": "read_keyword_weights_keyword_weights__get",
                }
            }
        },
    }