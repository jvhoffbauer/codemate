@needs_py310
def test_openapi_schema(client: TestClient):
    response = client.get("/openapi.json")
    assert response.status_code == 200, response.text
    assert response.json() == {
        "openapi": "3.1.0",
        "info": {"title": "FastAPI", "version": "0.1.0"},
        "paths": {
            "/items/{item_id}": {
                "put": {
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
                    "summary": "Read Items",
                    "operationId": "read_items_items__item_id__put",
                    "parameters": [
                        {
                            "required": True,
                            "schema": {
                                "title": "Item Id",
                                "type": "string",
                                "format": "uuid",
                            },
                            "name": "item_id",
                            "in": "path",
                        }
                    ],
                    "requestBody": {
                        "content": {
                            "application/json": {
                                "schema": IsDict(
                                    {
                                        "allOf": [
                                            {
                                                "$ref": "#/components/schemas/Body_read_items_items__item_id__put"
                                            }
                                        ],
                                        "title": "Body",
                                    }
                                )
                                | IsDict(
                                    # TODO: remove when deprecating Pydantic v1
                                    {
                                        "$ref": "#/components/schemas/Body_read_items_items__item_id__put"
                                    }
                                )
                            }
                        }
                    },
                }
            }
        },
        "components": {
            "schemas": {
                "Body_read_items_items__item_id__put": {
                    "title": "Body_read_items_items__item_id__put",
                    "type": "object",
                    "properties": {
                        "start_datetime": IsDict(
                            {
                                "title": "Start Datetime",
                                "anyOf": [
                                    {"type": "string", "format": "date-time"},
                                    {"type": "null"},
                                ],
                            }
                        )
                        | IsDict(
                            # TODO: remove when deprecating Pydantic v1
                            {
                                "title": "Start Datetime",
                                "type": "string",
                                "format": "date-time",
                            }
                        ),
                        "end_datetime": IsDict(
                            {
                                "title": "End Datetime",
                                "anyOf": [
                                    {"type": "string", "format": "date-time"},
                                    {"type": "null"},
                                ],
                            }
                        )
                        | IsDict(
                            # TODO: remove when deprecating Pydantic v1
                            {
                                "title": "End Datetime",
                                "type": "string",
                                "format": "date-time",
                            }
                        ),
                        "repeat_at": IsDict(
                            {
                                "title": "Repeat At",
                                "anyOf": [
                                    {"type": "string", "format": "time"},
                                    {"type": "null"},
                                ],
                            }
                        )
                        | IsDict(
                            # TODO: remove when deprecating Pydantic v1
                            {
                                "title": "Repeat At",
                                "type": "string",
                                "format": "time",
                            }
                        ),
                        "process_after": IsDict(
                            {
                                "title": "Process After",
                                "anyOf": [
                                    {"type": "string", "format": "duration"},
                                    {"type": "null"},
                                ],
                            }
                        )
                        | IsDict(
                            # TODO: remove when deprecating Pydantic v1
                            {
                                "title": "Process After",
                                "type": "number",
                                "format": "time-delta",
                            }
                        ),
                    },
                },
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
            }
        },
    }