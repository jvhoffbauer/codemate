def test_openapi_schema(client: TestClient):
    response = client.get("/openapi.json")
    assert response.status_code == 200, response.text
    assert response.json() == {
        "openapi": "3.1.0",
        "info": {"title": "FastAPI", "version": "0.1.0"},
        "paths": {
            "/": {
                "get": {
                    "summary": "Read Root",
                    "operationId": "read_root__get",
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {
                                "application/json": {
                                    "schema": {"$ref": "#/components/schemas/Rectangle"}
                                }
                            },
                        }
                    },
                }
            }
        },
        "components": {
            "schemas": {
                "Rectangle": {
                    "properties": {
                        "width": {"type": "integer", "title": "Width"},
                        "length": {"type": "integer", "title": "Length"},
                        "area": {"type": "integer", "title": "Area", "readOnly": True},
                    },
                    "type": "object",
                    "required": ["width", "length", "area"],
                    "title": "Rectangle",
                }
            }
        },
    }