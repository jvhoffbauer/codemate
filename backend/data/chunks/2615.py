def test_openapi_schema():
    response = client.get("/openapi.json")
    assert response.status_code == 200, response.text
    assert response.json() == {
        "openapi": "3.1.0",
        "info": {"title": "FastAPI", "version": "0.1.0"},
        "paths": {
            "/model-with-tuple/": {
                "post": {
                    "summary": "Post Model With Tuple",
                    "operationId": "post_model_with_tuple_model_with_tuple__post",
                    "requestBody": {
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/ItemGroup"}
                            }
                        },
                        "required": True,
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
            },
            "/tuple-of-models/": {
                "post": {
                    "summary": "Post Tuple Of Models",
                    "operationId": "post_tuple_of_models_tuple_of_models__post",
                    "requestBody": {
                        "content": {
                            "application/json": {
                                "schema": IsDict(
                                    {
                                        "title": "Square",
                                        "maxItems": 2,
                                        "minItems": 2,
                                        "type": "array",
                                        "prefixItems": [
                                            {"$ref": "#/components/schemas/Coordinate"},
                                            {"$ref": "#/components/schemas/Coordinate"},
                                        ],
                                    }
                                )
                                | IsDict(
                                    # TODO: remove when deprecating Pydantic v1
                                    {
                                        "title": "Square",
                                        "maxItems": 2,
                                        "minItems": 2,
                                        "type": "array",
                                        "items": [
                                            {"$ref": "#/components/schemas/Coordinate"},
                                            {"$ref": "#/components/schemas/Coordinate"},
                                        ],
                                    }
                                )
                            }
                        },
                        "required": True,
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
            },
            "/tuple-form/": {
                "post": {
                    "summary": "Hello",
                    "operationId": "hello_tuple_form__post",
                    "requestBody": {
                        "content": {
                            "application/x-www-form-urlencoded": {
                                "schema": {
                                    "$ref": "#/components/schemas/Body_hello_tuple_form__post"
                                }
                            }
                        },
                        "required": True,
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
            },
        },
        "components": {
            "schemas": {
                "Body_hello_tuple_form__post": {
                    "title": "Body_hello_tuple_form__post",
                    "required": ["values"],
                    "type": "object",
                    "properties": {
                        "values": IsDict(
                            {
                                "title": "Values",
                                "maxItems": 2,
                                "minItems": 2,
                                "type": "array",
                                "prefixItems": [
                                    {"type": "integer"},
                                    {"type": "integer"},
                                ],
                            }
                        )
                        | IsDict(
                            # TODO: remove when deprecating Pydantic v1
                            {
                                "title": "Values",
                                "maxItems": 2,
                                "minItems": 2,
                                "type": "array",
                                "items": [{"type": "integer"}, {"type": "integer"}],
                            }
                        )
                    },
                },
                "Coordinate": {
                    "title": "Coordinate",
                    "required": ["x", "y"],
                    "type": "object",
                    "properties": {
                        "x": {"title": "X", "type": "number"},
                        "y": {"title": "Y", "type": "number"},
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
                "ItemGroup": {
                    "title": "ItemGroup",
                    "required": ["items"],
                    "type": "object",
                    "properties": {
                        "items": {
                            "title": "Items",
                            "type": "array",
                            "items": IsDict(
                                {
                                    "maxItems": 2,
                                    "minItems": 2,
                                    "type": "array",
                                    "prefixItems": [
                                        {"type": "string"},
                                        {"type": "string"},
                                    ],
                                }
                            )
                            | IsDict(
                                # TODO: remove when deprecating Pydantic v1
                                {
                                    "maxItems": 2,
                                    "minItems": 2,
                                    "type": "array",
                                    "items": [{"type": "string"}, {"type": "string"}],
                                }
                            ),
                        }
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
            }
        },
    }