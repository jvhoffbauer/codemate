def test_callback_override_generate_unique_id():
    app = FastAPI(generate_unique_id_function=custom_generate_unique_id)
    callback_router = APIRouter(generate_unique_id_function=custom_generate_unique_id2)

    @callback_router.post(
        "/post-callback",
        response_model=List[Item],
        responses={404: {"model": List[Message]}},
        generate_unique_id_function=custom_generate_unique_id3,
    )
    def post_callback(item1: Item, item2: Item):
        return item1, item2  # pragma: nocover

    @app.post(
        "/",
        response_model=List[Item],
        responses={404: {"model": List[Message]}},
        generate_unique_id_function=custom_generate_unique_id3,
        callbacks=callback_router.routes,
    )
    def post_root(item1: Item, item2: Item):
        return item1, item2  # pragma: nocover

    @app.post(
        "/tocallback",
        response_model=List[Item],
        responses={404: {"model": List[Message]}},
    )
    def post_with_callback(item1: Item, item2: Item):
        return item1, item2  # pragma: nocover

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
                    "callbacks": {
                        "post_callback": {
                            "/post-callback": {
                                "post": {
                                    "summary": "Post Callback",
                                    "operationId": "baz_post_callback",
                                    "requestBody": {
                                        "content": {
                                            "application/json": {
                                                "schema": {
                                                    "$ref": "#/components/schemas/Body_baz_post_callback"
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
                                                        "title": "Response Baz Post Callback",
                                                        "type": "array",
                                                        "items": {
                                                            "$ref": "#/components/schemas/Item"
                                                        },
                                                    }
                                                }
                                            },
                                        },
                                        "404": {
                                            "description": "Not Found",
                                            "content": {
                                                "application/json": {
                                                    "schema": {
                                                        "title": "Response 404 Baz Post Callback",
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
                            }
                        }
                    },
                }
            },
            "/tocallback": {
                "post": {
                    "summary": "Post With Callback",
                    "operationId": "foo_post_with_callback",
                    "requestBody": {
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/Body_foo_post_with_callback"
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
                                        "title": "Response Foo Post With Callback",
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
                                        "title": "Response 404 Foo Post With Callback",
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
                "Body_baz_post_callback": {
                    "title": "Body_baz_post_callback",
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
                "Body_foo_post_with_callback": {
                    "title": "Body_foo_post_with_callback",
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