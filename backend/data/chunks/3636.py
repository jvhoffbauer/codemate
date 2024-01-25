@needs_py310
def test_openapi_schema():
    client = get_client()
    response = client.get("/openapi.json")
    assert response.status_code == 200, response.text
    # insert_assert(response.json())
    assert response.json() == {
        "openapi": "3.1.0",
        "info": {"title": "FastAPI", "version": "0.1.0"},
        "paths": {
            "/items/": {
                "post": {
                    "summary": "Read Items",
                    "operationId": "read_items_items__post",
                    "requestBody": {
                        "content": {
                            "application/x-www-form-urlencoded": {
                                "schema": IsDict(
                                    {
                                        "allOf": [
                                            {
                                                "$ref": "#/components/schemas/Body_read_items_items__post"
                                            }
                                        ],
                                        "title": "Body",
                                    }
                                )
                                | IsDict(
                                    # TODO: remove when deprecating Pydantic v1
                                    {
                                        "$ref": "#/components/schemas/Body_read_items_items__post"
                                    }
                                )
                            }
                        }
                    },
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
                "Body_read_items_items__post": {
                    "properties": {
                        "q": IsDict(
                            {
                                "anyOf": [
                                    {"type": "string", "pattern": "^fixedquery$"},
                                    {"type": "null"},
                                ],
                                "title": "Q",
                            }
                        )
                        | IsDict(
                            # TODO: remove when deprecating Pydantic v1
                            {"type": "string", "pattern": "^fixedquery$", "title": "Q"}
                        )
                    },
                    "type": "object",
                    "title": "Body_read_items_items__post",
                },
                "HTTPValidationError": {
                    "properties": {
                        "detail": {
                            "items": {"$ref": "#/components/schemas/ValidationError"},
                            "type": "array",
                            "title": "Detail",
                        }
                    },
                    "type": "object",
                    "title": "HTTPValidationError",
                },
                "ValidationError": {
                    "properties": {
                        "loc": {
                            "items": {
                                "anyOf": [{"type": "string"}, {"type": "integer"}]
                            },
                            "type": "array",
                            "title": "Location",
                        },
                        "msg": {"type": "string", "title": "Message"},
                        "type": {"type": "string", "title": "Error Type"},
                    },
                    "type": "object",
                    "required": ["loc", "msg", "type"],
                    "title": "ValidationError",
                },
            }
        },
    }