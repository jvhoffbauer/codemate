def test_openapi_schema():
    response = client.get("/openapi.json")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data == {
        "openapi": "3.1.0",
        "info": {"title": "FastAPI", "version": "0.1.0"},
        "paths": {
            "/models/{model_name}": {
                "get": {
                    "summary": "Get Model",
                    "operationId": "get_model_models__model_name__get",
                    "parameters": [
                        {
                            "required": True,
                            "schema": {"$ref": "#/components/schemas/ModelName"},
                            "name": "model_name",
                            "in": "path",
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/json": {"schema": {}}},
                        },
                        "422": {
                            "description": "Validation Error",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "$ref": "#/components/schemas/HTTPValidationError"
                                    }
                                }
                            },
                        },
                    },
                }
            }
        },
        "components": {
            "schemas": {
                "HTTPValidationError": {
                    "title": "HTTPValidationError",
                    "type": "object",
                    "properties": {
                        "detail": {
                            "title": "Detail",
                            "type": "array",
                            "items": {"$ref": "#/components/schemas/ValidationError"},
                        }
                    },
                },
                "ModelName": IsDict(
                    {
                        "title": "ModelName",
                        "enum": ["alexnet", "resnet", "lenet"],
                        "type": "string",
                    }
                )
                | IsDict(
                    {
                        # TODO: remove when deprecating Pydantic v1
                        "title": "ModelName",
                        "enum": ["alexnet", "resnet", "lenet"],
                        "type": "string",
                        "description": "An enumeration.",
                    }
                ),
                "ValidationError": {
                    "title": "ValidationError",
                    "required": ["loc", "msg", "type"],
                    "type": "object",
                    "properties": {
                        "loc": {
                            "title": "Location",
                            "type": "array",
                            "items": {
                                "anyOf": [{"type": "string"}, {"type": "integer"}]
                            },
                        },
                        "msg": {"title": "Message", "type": "string"},
                        "type": {"title": "Error Type", "type": "string"},
                    },
                },
            }
        },
    }