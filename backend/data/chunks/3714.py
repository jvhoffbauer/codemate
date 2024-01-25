def test_openapi_schema():
    response = client.get("/openapi.json")
    assert response.status_code == 200, response.text
    assert response.json() == {
        "openapi": "3.1.0",
        "info": {"title": "FastAPI", "version": "0.1.0"},
        "paths": {
            "/examples/": {
                "post": {
                    "summary": "Examples",
                    "operationId": "examples_examples__post",
                    "requestBody": {
                        "content": {
                            "application/json": {
                                "schema": {
                                    "allOf": [{"$ref": "#/components/schemas/Item"}],
                                    "title": "Item",
                                    "examples": [
                                        {"data": "Data in Body examples, example1"}
                                    ],
                                },
                                "examples": {
                                    "Example One": {
                                        "summary": "Example One Summary",
                                        "description": "Example One Description",
                                        "value": {
                                            "data": "Data in Body examples, example1"
                                        },
                                    },
                                    "Example Two": {
                                        "value": {
                                            "data": "Data in Body examples, example2"
                                        }
                                    },
                                },
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
            "/path_examples/{item_id}": {
                "get": {
                    "summary": "Path Examples",
                    "operationId": "path_examples_path_examples__item_id__get",
                    "parameters": [
                        {
                            "name": "item_id",
                            "in": "path",
                            "required": True,
                            "schema": {
                                "type": "string",
                                "examples": [
                                    "json_schema_item_1",
                                    "json_schema_item_2",
                                ],
                                "title": "Item Id",
                            },
                            "examples": {
                                "Path One": {
                                    "summary": "Path One Summary",
                                    "description": "Path One Description",
                                    "value": "item_1",
                                },
                                "Path Two": {"value": "item_2"},
                            },
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
            },
            "/query_examples/": {
                "get": {
                    "summary": "Query Examples",
                    "operationId": "query_examples_query_examples__get",
                    "parameters": [
                        {
                            "name": "data",
                            "in": "query",
                            "required": False,
                            "schema": IsDict(
                                {
                                    "anyOf": [{"type": "string"}, {"type": "null"}],
                                    "examples": [
                                        "json_schema_query1",
                                        "json_schema_query2",
                                    ],
                                    "title": "Data",
                                }
                            )
                            | IsDict(
                                # TODO: remove when deprecating Pydantic v1
                                {
                                    "examples": [
                                        "json_schema_query1",
                                        "json_schema_query2",
                                    ],
                                    "type": "string",
                                    "title": "Data",
                                }
                            ),
                            "examples": {
                                "Query One": {
                                    "summary": "Query One Summary",
                                    "description": "Query One Description",
                                    "value": "query1",
                                },
                                "Query Two": {"value": "query2"},
                            },
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
            },
            "/header_examples/": {
                "get": {
                    "summary": "Header Examples",
                    "operationId": "header_examples_header_examples__get",
                    "parameters": [
                        {
                            "name": "data",
                            "in": "header",
                            "required": False,
                            "schema": IsDict(
                                {
                                    "anyOf": [{"type": "string"}, {"type": "null"}],
                                    "examples": [
                                        "json_schema_header1",
                                        "json_schema_header2",
                                    ],
                                    "title": "Data",
                                }
                            )
                            | IsDict(
                                # TODO: remove when deprecating Pydantic v1
                                {
                                    "type": "string",
                                    "examples": [
                                        "json_schema_header1",
                                        "json_schema_header2",
                                    ],
                                    "title": "Data",
                                }
                            ),
                            "examples": {
                                "Header One": {
                                    "summary": "Header One Summary",
                                    "description": "Header One Description",
                                    "value": "header1",
                                },
                                "Header Two": {"value": "header2"},
                            },
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
            },
            "/cookie_examples/": {
                "get": {
                    "summary": "Cookie Examples",
                    "operationId": "cookie_examples_cookie_examples__get",
                    "parameters": [
                        {
                            "name": "data",
                            "in": "cookie",
                            "required": False,
                            "schema": IsDict(
                                {
                                    "anyOf": [{"type": "string"}, {"type": "null"}],
                                    "examples": [
                                        "json_schema_cookie1",
                                        "json_schema_cookie2",
                                    ],
                                    "title": "Data",
                                }
                            )
                            | IsDict(
                                # TODO: remove when deprecating Pydantic v1
                                {
                                    "type": "string",
                                    "examples": [
                                        "json_schema_cookie1",
                                        "json_schema_cookie2",
                                    ],
                                    "title": "Data",
                                }
                            ),
                            "examples": {
                                "Cookie One": {
                                    "summary": "Cookie One Summary",
                                    "description": "Cookie One Description",
                                    "value": "cookie1",
                                },
                                "Cookie Two": {"value": "cookie2"},
                            },
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
            },
        },
        "components": {
            "schemas": {
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
                "Item": {
                    "properties": {"data": {"type": "string", "title": "Data"}},
                    "type": "object",
                    "required": ["data"],
                    "title": "Item",
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