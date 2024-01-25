def test_openapi_schema():
    client = get_app_client()
    response = client.get("/openapi.json")
    assert response.status_code == 200, response.text
    assert response.json() == {
        "openapi": "3.1.0",
        "info": {"title": "FastAPI", "version": "0.1.0"},
        "paths": {
            "/items/": {
                "get": {
                    "summary": "Read Items",
                    "operationId": "read_items_items__get",
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "items": {
                                            "$ref": "#/components/schemas/Item-Output"
                                        },
                                        "type": "array",
                                        "title": "Response Read Items Items  Get",
                                    }
                                }
                            },
                        }
                    },
                },
                "post": {
                    "summary": "Create Item",
                    "operationId": "create_item_items__post",
                    "requestBody": {
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/Item-Input"}
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
                },
            },
            "/items-list/": {
                "post": {
                    "summary": "Create Item List",
                    "operationId": "create_item_list_items_list__post",
                    "requestBody": {
                        "content": {
                            "application/json": {
                                "schema": {
                                    "items": {
                                        "$ref": "#/components/schemas/Item-Input"
                                    },
                                    "type": "array",
                                    "title": "Item",
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
                "Item-Input": {
                    "properties": {
                        "name": {"type": "string", "title": "Name"},
                        "description": {
                            "anyOf": [{"type": "string"}, {"type": "null"}],
                            "title": "Description",
                        },
                        "sub": {
                            "anyOf": [
                                {"$ref": "#/components/schemas/SubItem-Input"},
                                {"type": "null"},
                            ]
                        },
                    },
                    "type": "object",
                    "required": ["name"],
                    "title": "Item",
                },
                "Item-Output": {
                    "properties": {
                        "name": {"type": "string", "title": "Name"},
                        "description": {
                            "anyOf": [{"type": "string"}, {"type": "null"}],
                            "title": "Description",
                        },
                        "sub": {
                            "anyOf": [
                                {"$ref": "#/components/schemas/SubItem-Output"},
                                {"type": "null"},
                            ]
                        },
                    },
                    "type": "object",
                    "required": ["name", "description", "sub"],
                    "title": "Item",
                },
                "SubItem-Input": {
                    "properties": {
                        "subname": {"type": "string", "title": "Subname"},
                        "sub_description": {
                            "anyOf": [{"type": "string"}, {"type": "null"}],
                            "title": "Sub Description",
                        },
                        "tags": {
                            "items": {"type": "string"},
                            "type": "array",
                            "title": "Tags",
                            "default": [],
                        },
                    },
                    "type": "object",
                    "required": ["subname"],
                    "title": "SubItem",
                },
                "SubItem-Output": {
                    "properties": {
                        "subname": {"type": "string", "title": "Subname"},
                        "sub_description": {
                            "anyOf": [{"type": "string"}, {"type": "null"}],
                            "title": "Sub Description",
                        },
                        "tags": {
                            "items": {"type": "string"},
                            "type": "array",
                            "title": "Tags",
                            "default": [],
                        },
                    },
                    "type": "object",
                    "required": ["subname", "sub_description", "tags"],
                    "title": "SubItem",
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