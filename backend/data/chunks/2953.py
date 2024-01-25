def test_openapi_schema():
    response = client.get("/openapi.json")
    assert response.status_code == 200, response.text
    assert response.json() == {
        "openapi": "3.1.0",
        "info": {"title": "FastAPI", "version": "0.1.0"},
        "paths": {
            "/": {
                "get": {
                    "summary": "F",
                    "operationId": "f__get",
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {
                                "application/json": {
                                    "schema": {"$ref": "#/components/schemas/Model3"}
                                }
                            },
                        }
                    },
                }
            }
        },
        "components": {
            "schemas": {
                "Model": {"title": "Model", "type": "object", "properties": {}},
                "Model2": {
                    "title": "Model2",
                    "required": ["a"],
                    "type": "object",
                    "properties": {"a": {"$ref": "#/components/schemas/Model"}},
                },
                "Model3": {
                    "title": "Model3",
                    "required": ["c", "d"],
                    "type": "object",
                    "properties": {
                        "c": {"$ref": "#/components/schemas/Model"},
                        "d": {"$ref": "#/components/schemas/Model2"},
                    },
                },
            }
        },
    }