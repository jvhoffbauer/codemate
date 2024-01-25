def test_app_path_operation_overrides_generate_unique_id():
    app = FastAPI(generate_unique_id_function=custom_generate_unique_id)
    router = APIRouter(generate_unique_id_function=custom_generate_unique_id2)

    @app.post(
        "/",
        response_model=List[Item],
        responses={404: {"model": List[Message]}},
        generate_unique_id_function=custom_generate_unique_id3,
    )
    def post_root(item1: Item, item2: Item):
        return item1, item2  # pragma: nocover

    @router.post(
        "/router",
        response_model=List[Item],
        responses={404: {"model": List[Message]}},
    )
    def post_router(item1: Item, item2: Item):
        return item1, item2  # pragma: nocover

    app.include_router(router)
    client = TestClient(app)
    response = client.get("/openapi.json")
    data = response.json()
    assert data == {
        "openapi": "3.1.0",
        "info": {"title": "FastAPI", "version": "0.1.0"},
        "paths": {
            "/": {
                "post": {
                    "summary": "Post Root",
                    "operationId": "baz_post_root",
                    "requestBody": {
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/Body_baz_post_root"
                                }
                            }
                        },
                        "required": True,
                    },
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "title": "Response Baz Post Root",
                                        "type": "array",
                                        "items": {"$ref": "#/components/schemas/Item"},
                                    }
                                }
                            },
                        },
                        "404": {
                            "description": "Not Found",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "title": "Response 404 Baz Post Root",
                                        "type": "array",
                                        "items": {
                                            "$ref": "#/components/schemas/Message"
                                        },
                                    }
                                }
                            },
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
            "/router": {
                "post": {
                    "summary": "Post Router",
                    "operationId": "bar_post_router",
                    "requestBody": {
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/Body_bar_post_router"
                                }
                            }
                        },
                        "required": True,
                    },
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "title": "Response Bar Post Router",
                                        "type": "array",
                                        "items": {"$ref": "#/components/schemas/Item"},
                                    }
                                }
                            },
                        },
                        "404": {
                            "description": "Not Found",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "title": "Response 404 Bar Post Router",
                                        "type": "array",
                                        "items": {
                                            "$ref": "#/components/schemas/Message"
                                        },
                                    }
                                }
                            },
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
                "Body_bar_post_router": {
                    "title": "Body_bar_post_router",
                    "required": ["item1", "item2"],
                    "type": "object",
                    "properties": {
                        "item1": {"$ref": "#/components/schemas/Item"},
                        "item2": {"$ref": "#/components/schemas/Item"},
                    },
                },
                "Body_baz_post_root": {
                    "title": "Body_baz_post_root",
                    "required": ["item1", "item2"],
                    "type": "object",
                    "properties": {
                        "item1": {"$ref": "#/components/schemas/Item"},
                        "item2": {"$ref": "#/components/schemas/Item"},
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
                "Item": {
                    "title": "Item",
                    "required": ["name", "price"],
                    "type": "object",
                    "properties": {
                        "name": {"title": "Name", "type": "string"},
                        "price": {"title": "Price", "type": "number"},
                    },
                },
                "Message": {
                    "title": "Message",
                    "required": ["title", "description"],
                    "type": "object",
                    "properties": {
                        "title": {"title": "Title", "type": "string"},
                        "description": {"title": "Description", "type": "string"},
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