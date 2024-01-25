def test_openapi_schema():
    response = client.get("/openapi.json")
    assert response.status_code == 200, response.text
    assert response.json() == {
        "openapi": "3.1.0",
        "info": {"title": "FastAPI", "version": "0.1.0"},
        "paths": {
            "/a": {
                "get": {
                    "responses": {
                        "500": {
                            "description": "Error",
                            "content": {
                                "application/vnd.api+json": {
                                    "schema": {
                                        "$ref": "#/components/schemas/JsonApiError"
                                    }
                                }
                            },
                        },
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/vnd.api+json": {"schema": {}}},
                        },
                    },
                    "summary": "A",
                    "operationId": "a_a_get",
                }
            },
            "/b": {
                "get": {
                    "responses": {
                        "500": {
                            "description": "Error",
                            "content": {
                                "application/json": {
                                    "schema": {"$ref": "#/components/schemas/Error"}
                                }
                            },
                        },
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/json": {"schema": {}}},
                        },
                    },
                    "summary": "B",
                    "operationId": "b_b_get",
                }
            },
        },
        "components": {
            "schemas": {
                "Error": {
                    "title": "Error",
                    "required": ["status", "title"],
                    "type": "object",
                    "properties": {
                        "status": {"title": "Status", "type": "string"},
                        "title": {"title": "Title", "type": "string"},
                    },
                },
                "JsonApiError": {
                    "title": "JsonApiError",
                    "required": ["errors"],
                    "type": "object",
                    "properties": {
                        "errors": {
                            "title": "Errors",
                            "type": "array",
                            "items": {"$ref": "#/components/schemas/Error"},
                        }
                    },
                },
            }
        },
    }