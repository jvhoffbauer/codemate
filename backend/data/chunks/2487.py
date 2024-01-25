def test_openapi():
    client = TestClient(app)
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        response = client.get("/openapi.json")
        assert issubclass(w[-1].category, UserWarning)
        assert "Duplicate Operation ID" in str(w[-1].message)
    assert response.json() == {
        "openapi": "3.1.0",
        "info": {"title": "FastAPI", "version": "0.1.0"},
        "paths": {
            "/override1": {
                "get": {
                    "tags": ["path1a", "path1b"],
                    "summary": "Path1 Override",
                    "operationId": "path1_override_override1_get",
                    "parameters": [
                        {
                            "required": True,
                            "schema": {"title": "Level1", "type": "string"},
                            "name": "level1",
                            "in": "query",
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/x-level-1": {"schema": {}}},
                        },
                        "400": {"description": "Client error level 0"},
                        "401": {"description": "Client error level 1"},
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
                        "500": {"description": "Server error level 0"},
                        "501": {"description": "Server error level 1"},
                    },
                    "callbacks": {
                        "callback0": {
                            "/": {
                                "get": {
                                    "summary": "Callback0",
                                    "operationId": "callback0__get",
                                    "parameters": [
                                        {
                                            "name": "level0",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level0",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback1": {
                            "/": {
                                "get": {
                                    "summary": "Callback1",
                                    "operationId": "callback1__get",
                                    "parameters": [
                                        {
                                            "name": "level1",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level1",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                    },
                    "deprecated": True,
                }
            },
            "/default1": {
                "get": {
                    "summary": "Path1 Default",
                    "operationId": "path1_default_default1_get",
                    "parameters": [
                        {
                            "required": True,
                            "schema": {"title": "Level1", "type": "string"},
                            "name": "level1",
                            "in": "query",
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/x-level-0": {"schema": {}}},
                        },
                        "400": {"description": "Client error level 0"},
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
                        "500": {"description": "Server error level 0"},
                    },
                    "callbacks": {
                        "callback0": {
                            "/": {
                                "get": {
                                    "summary": "Callback0",
                                    "operationId": "callback0__get",
                                    "parameters": [
                                        {
                                            "name": "level0",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level0",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
            "/level1/level2/override3": {
                "get": {
                    "tags": [
                        "level1a",
                        "level1b",
                        "level2a",
                        "level2b",
                        "path3a",
                        "path3b",
                    ],
                    "summary": "Path3 Override Router2 Override",
                    "operationId": "path3_override_router2_override_level1_level2_override3_get",
                    "parameters": [
                        {
                            "required": True,
                            "schema": {"title": "Level3", "type": "string"},
                            "name": "level3",
                            "in": "query",
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/x-level-3": {"schema": {}}},
                        },
                        "400": {"description": "Client error level 0"},
                        "401": {"description": "Client error level 1"},
                        "402": {"description": "Client error level 2"},
                        "403": {"description": "Client error level 3"},
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
                        "500": {"description": "Server error level 0"},
                        "501": {"description": "Server error level 1"},
                        "502": {"description": "Server error level 2"},
                        "503": {"description": "Server error level 3"},
                    },
                    "callbacks": {
                        "callback0": {
                            "/": {
                                "get": {
                                    "summary": "Callback0",
                                    "operationId": "callback0__get",
                                    "parameters": [
                                        {
                                            "name": "level0",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level0",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback1": {
                            "/": {
                                "get": {
                                    "summary": "Callback1",
                                    "operationId": "callback1__get",
                                    "parameters": [
                                        {
                                            "name": "level1",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level1",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback2": {
                            "/": {
                                "get": {
                                    "summary": "Callback2",
                                    "operationId": "callback2__get",
                                    "parameters": [
                                        {
                                            "name": "level2",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level2",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback3": {
                            "/": {
                                "get": {
                                    "summary": "Callback3",
                                    "operationId": "callback3__get",
                                    "parameters": [
                                        {
                                            "name": "level3",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level3",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                    },
                    "deprecated": True,
                }
            },
            "/level1/level2/default3": {
                "get": {
                    "tags": ["level1a", "level1b", "level2a", "level2b"],
                    "summary": "Path3 Default Router2 Override",
                    "operationId": "path3_default_router2_override_level1_level2_default3_get",
                    "parameters": [
                        {
                            "required": True,
                            "schema": {"title": "Level3", "type": "string"},
                            "name": "level3",
                            "in": "query",
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/x-level-2": {"schema": {}}},
                        },
                        "400": {"description": "Client error level 0"},
                        "401": {"description": "Client error level 1"},
                        "402": {"description": "Client error level 2"},
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
                        "500": {"description": "Server error level 0"},
                        "501": {"description": "Server error level 1"},
                        "502": {"description": "Server error level 2"},
                    },
                    "callbacks": {
                        "callback0": {
                            "/": {
                                "get": {
                                    "summary": "Callback0",
                                    "operationId": "callback0__get",
                                    "parameters": [
                                        {
                                            "name": "level0",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level0",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback1": {
                            "/": {
                                "get": {
                                    "summary": "Callback1",
                                    "operationId": "callback1__get",
                                    "parameters": [
                                        {
                                            "name": "level1",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level1",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback2": {
                            "/": {
                                "get": {
                                    "summary": "Callback2",
                                    "operationId": "callback2__get",
                                    "parameters": [
                                        {
                                            "name": "level2",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level2",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                    },
                    "deprecated": True,
                }
            },
            "/level1/level2/level3/level4/override5": {
                "get": {
                    "tags": [
                        "level1a",
                        "level1b",
                        "level2a",
                        "level2b",
                        "level3a",
                        "level3b",
                        "level4a",
                        "level4b",
                        "path5a",
                        "path5b",
                    ],
                    "summary": "Path5 Override Router4 Override",
                    "operationId": "path5_override_router4_override_level1_level2_level3_level4_override5_get",
                    "parameters": [
                        {
                            "required": True,
                            "schema": {"title": "Level5", "type": "string"},
                            "name": "level5",
                            "in": "query",
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/x-level-5": {"schema": {}}},
                        },
                        "400": {"description": "Client error level 0"},
                        "401": {"description": "Client error level 1"},
                        "402": {"description": "Client error level 2"},
                        "403": {"description": "Client error level 3"},
                        "404": {"description": "Client error level 4"},
                        "405": {"description": "Client error level 5"},
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
                        "500": {"description": "Server error level 0"},
                        "501": {"description": "Server error level 1"},
                        "502": {"description": "Server error level 2"},
                        "503": {"description": "Server error level 3"},
                        "504": {"description": "Server error level 4"},
                        "505": {"description": "Server error level 5"},
                    },
                    "callbacks": {
                        "callback0": {
                            "/": {
                                "get": {
                                    "summary": "Callback0",
                                    "operationId": "callback0__get",
                                    "parameters": [
                                        {
                                            "name": "level0",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level0",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback1": {
                            "/": {
                                "get": {
                                    "summary": "Callback1",
                                    "operationId": "callback1__get",
                                    "parameters": [
                                        {
                                            "name": "level1",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level1",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback2": {
                            "/": {
                                "get": {
                                    "summary": "Callback2",
                                    "operationId": "callback2__get",
                                    "parameters": [
                                        {
                                            "name": "level2",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level2",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback3": {
                            "/": {
                                "get": {
                                    "summary": "Callback3",
                                    "operationId": "callback3__get",
                                    "parameters": [
                                        {
                                            "name": "level3",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level3",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback4": {
                            "/": {
                                "get": {
                                    "summary": "Callback4",
                                    "operationId": "callback4__get",
                                    "parameters": [
                                        {
                                            "name": "level4",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level4",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback5": {
                            "/": {
                                "get": {
                                    "summary": "Callback5",
                                    "operationId": "callback5__get",
                                    "parameters": [
                                        {
                                            "name": "level5",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level5",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                    },
                    "deprecated": True,
                }
            },
            "/level1/level2/level3/level4/default5": {
                "get": {
                    "tags": [
                        "level1a",
                        "level1b",
                        "level2a",
                        "level2b",
                        "level3a",
                        "level3b",
                        "level4a",
                        "level4b",
                    ],
                    "summary": "Path5 Default Router4 Override",
                    "operationId": "path5_default_router4_override_level1_level2_level3_level4_default5_get",
                    "parameters": [
                        {
                            "required": True,
                            "schema": {"title": "Level5", "type": "string"},
                            "name": "level5",
                            "in": "query",
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/x-level-4": {"schema": {}}},
                        },
                        "400": {"description": "Client error level 0"},
                        "401": {"description": "Client error level 1"},
                        "402": {"description": "Client error level 2"},
                        "403": {"description": "Client error level 3"},
                        "404": {"description": "Client error level 4"},
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
                        "500": {"description": "Server error level 0"},
                        "501": {"description": "Server error level 1"},
                        "502": {"description": "Server error level 2"},
                        "503": {"description": "Server error level 3"},
                        "504": {"description": "Server error level 4"},
                    },
                    "callbacks": {
                        "callback0": {
                            "/": {
                                "get": {
                                    "summary": "Callback0",
                                    "operationId": "callback0__get",
                                    "parameters": [
                                        {
                                            "name": "level0",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level0",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback1": {
                            "/": {
                                "get": {
                                    "summary": "Callback1",
                                    "operationId": "callback1__get",
                                    "parameters": [
                                        {
                                            "name": "level1",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level1",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback2": {
                            "/": {
                                "get": {
                                    "summary": "Callback2",
                                    "operationId": "callback2__get",
                                    "parameters": [
                                        {
                                            "name": "level2",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level2",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback3": {
                            "/": {
                                "get": {
                                    "summary": "Callback3",
                                    "operationId": "callback3__get",
                                    "parameters": [
                                        {
                                            "name": "level3",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level3",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback4": {
                            "/": {
                                "get": {
                                    "summary": "Callback4",
                                    "operationId": "callback4__get",
                                    "parameters": [
                                        {
                                            "name": "level4",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level4",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                    },
                    "deprecated": True,
                }
            },
            "/level1/level2/level3/override5": {
                "get": {
                    "tags": [
                        "level1a",
                        "level1b",
                        "level2a",
                        "level2b",
                        "level3a",
                        "level3b",
                        "path5a",
                        "path5b",
                    ],
                    "summary": "Path5 Override Router4 Default",
                    "operationId": "path5_override_router4_default_level1_level2_level3_override5_get",
                    "parameters": [
                        {
                            "required": True,
                            "schema": {"title": "Level5", "type": "string"},
                            "name": "level5",
                            "in": "query",
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/x-level-5": {"schema": {}}},
                        },
                        "400": {"description": "Client error level 0"},
                        "401": {"description": "Client error level 1"},
                        "402": {"description": "Client error level 2"},
                        "403": {"description": "Client error level 3"},
                        "405": {"description": "Client error level 5"},
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
                        "500": {"description": "Server error level 0"},
                        "501": {"description": "Server error level 1"},
                        "502": {"description": "Server error level 2"},
                        "503": {"description": "Server error level 3"},
                        "505": {"description": "Server error level 5"},
                    },
                    "callbacks": {
                        "callback0": {
                            "/": {
                                "get": {
                                    "summary": "Callback0",
                                    "operationId": "callback0__get",
                                    "parameters": [
                                        {
                                            "name": "level0",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level0",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback1": {
                            "/": {
                                "get": {
                                    "summary": "Callback1",
                                    "operationId": "callback1__get",
                                    "parameters": [
                                        {
                                            "name": "level1",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level1",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback2": {
                            "/": {
                                "get": {
                                    "summary": "Callback2",
                                    "operationId": "callback2__get",
                                    "parameters": [
                                        {
                                            "name": "level2",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level2",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback3": {
                            "/": {
                                "get": {
                                    "summary": "Callback3",
                                    "operationId": "callback3__get",
                                    "parameters": [
                                        {
                                            "name": "level3",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level3",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback5": {
                            "/": {
                                "get": {
                                    "summary": "Callback5",
                                    "operationId": "callback5__get",
                                    "parameters": [
                                        {
                                            "name": "level5",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level5",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                    },
                    "deprecated": True,
                }
            },
            "/level1/level2/level3/default5": {
                "get": {
                    "tags": [
                        "level1a",
                        "level1b",
                        "level2a",
                        "level2b",
                        "level3a",
                        "level3b",
                    ],
                    "summary": "Path5 Default Router4 Default",
                    "operationId": "path5_default_router4_default_level1_level2_level3_default5_get",
                    "parameters": [
                        {
                            "required": True,
                            "schema": {"title": "Level5", "type": "string"},
                            "name": "level5",
                            "in": "query",
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/x-level-3": {"schema": {}}},
                        },
                        "400": {"description": "Client error level 0"},
                        "401": {"description": "Client error level 1"},
                        "402": {"description": "Client error level 2"},
                        "403": {"description": "Client error level 3"},
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
                        "500": {"description": "Server error level 0"},
                        "501": {"description": "Server error level 1"},
                        "502": {"description": "Server error level 2"},
                        "503": {"description": "Server error level 3"},
                    },
                    "callbacks": {
                        "callback0": {
                            "/": {
                                "get": {
                                    "summary": "Callback0",
                                    "operationId": "callback0__get",
                                    "parameters": [
                                        {
                                            "name": "level0",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level0",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback1": {
                            "/": {
                                "get": {
                                    "summary": "Callback1",
                                    "operationId": "callback1__get",
                                    "parameters": [
                                        {
                                            "name": "level1",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level1",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback2": {
                            "/": {
                                "get": {
                                    "summary": "Callback2",
                                    "operationId": "callback2__get",
                                    "parameters": [
                                        {
                                            "name": "level2",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level2",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback3": {
                            "/": {
                                "get": {
                                    "summary": "Callback3",
                                    "operationId": "callback3__get",
                                    "parameters": [
                                        {
                                            "name": "level3",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level3",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                    },
                    "deprecated": True,
                }
            },
            "/level1/level2/level4/override5": {
                "get": {
                    "tags": [
                        "level1a",
                        "level1b",
                        "level2a",
                        "level2b",
                        "level4a",
                        "level4b",
                        "path5a",
                        "path5b",
                    ],
                    "summary": "Path5 Override Router4 Override",
                    "operationId": "path5_override_router4_override_level1_level2_level4_override5_get",
                    "parameters": [
                        {
                            "required": True,
                            "schema": {"title": "Level5", "type": "string"},
                            "name": "level5",
                            "in": "query",
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/x-level-5": {"schema": {}}},
                        },
                        "400": {"description": "Client error level 0"},
                        "401": {"description": "Client error level 1"},
                        "402": {"description": "Client error level 2"},
                        "404": {"description": "Client error level 4"},
                        "405": {"description": "Client error level 5"},
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
                        "500": {"description": "Server error level 0"},
                        "501": {"description": "Server error level 1"},
                        "502": {"description": "Server error level 2"},
                        "504": {"description": "Server error level 4"},
                        "505": {"description": "Server error level 5"},
                    },
                    "callbacks": {
                        "callback0": {
                            "/": {
                                "get": {
                                    "summary": "Callback0",
                                    "operationId": "callback0__get",
                                    "parameters": [
                                        {
                                            "name": "level0",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level0",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback1": {
                            "/": {
                                "get": {
                                    "summary": "Callback1",
                                    "operationId": "callback1__get",
                                    "parameters": [
                                        {
                                            "name": "level1",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level1",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback2": {
                            "/": {
                                "get": {
                                    "summary": "Callback2",
                                    "operationId": "callback2__get",
                                    "parameters": [
                                        {
                                            "name": "level2",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level2",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback4": {
                            "/": {
                                "get": {
                                    "summary": "Callback4",
                                    "operationId": "callback4__get",
                                    "parameters": [
                                        {
                                            "name": "level4",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level4",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback5": {
                            "/": {
                                "get": {
                                    "summary": "Callback5",
                                    "operationId": "callback5__get",
                                    "parameters": [
                                        {
                                            "name": "level5",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level5",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                    },
                    "deprecated": True,
                }
            },
            "/level1/level2/level4/default5": {
                "get": {
                    "tags": [
                        "level1a",
                        "level1b",
                        "level2a",
                        "level2b",
                        "level4a",
                        "level4b",
                    ],
                    "summary": "Path5 Default Router4 Override",
                    "operationId": "path5_default_router4_override_level1_level2_level4_default5_get",
                    "parameters": [
                        {
                            "required": True,
                            "schema": {"title": "Level5", "type": "string"},
                            "name": "level5",
                            "in": "query",
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/x-level-4": {"schema": {}}},
                        },
                        "400": {"description": "Client error level 0"},
                        "401": {"description": "Client error level 1"},
                        "402": {"description": "Client error level 2"},
                        "404": {"description": "Client error level 4"},
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
                        "500": {"description": "Server error level 0"},
                        "501": {"description": "Server error level 1"},
                        "502": {"description": "Server error level 2"},
                        "504": {"description": "Server error level 4"},
                    },
                    "callbacks": {
                        "callback0": {
                            "/": {
                                "get": {
                                    "summary": "Callback0",
                                    "operationId": "callback0__get",
                                    "parameters": [
                                        {
                                            "name": "level0",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level0",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback1": {
                            "/": {
                                "get": {
                                    "summary": "Callback1",
                                    "operationId": "callback1__get",
                                    "parameters": [
                                        {
                                            "name": "level1",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level1",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback2": {
                            "/": {
                                "get": {
                                    "summary": "Callback2",
                                    "operationId": "callback2__get",
                                    "parameters": [
                                        {
                                            "name": "level2",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level2",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback4": {
                            "/": {
                                "get": {
                                    "summary": "Callback4",
                                    "operationId": "callback4__get",
                                    "parameters": [
                                        {
                                            "name": "level4",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level4",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                    },
                    "deprecated": True,
                }
            },
            "/level1/level2/override5": {
                "get": {
                    "tags": [
                        "level1a",
                        "level1b",
                        "level2a",
                        "level2b",
                        "path5a",
                        "path5b",
                    ],
                    "summary": "Path5 Override Router4 Default",
                    "operationId": "path5_override_router4_default_level1_level2_override5_get",
                    "parameters": [
                        {
                            "required": True,
                            "schema": {"title": "Level5", "type": "string"},
                            "name": "level5",
                            "in": "query",
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/x-level-5": {"schema": {}}},
                        },
                        "400": {"description": "Client error level 0"},
                        "401": {"description": "Client error level 1"},
                        "402": {"description": "Client error level 2"},
                        "405": {"description": "Client error level 5"},
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
                        "500": {"description": "Server error level 0"},
                        "501": {"description": "Server error level 1"},
                        "502": {"description": "Server error level 2"},
                        "505": {"description": "Server error level 5"},
                    },
                    "callbacks": {
                        "callback0": {
                            "/": {
                                "get": {
                                    "summary": "Callback0",
                                    "operationId": "callback0__get",
                                    "parameters": [
                                        {
                                            "name": "level0",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level0",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback1": {
                            "/": {
                                "get": {
                                    "summary": "Callback1",
                                    "operationId": "callback1__get",
                                    "parameters": [
                                        {
                                            "name": "level1",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level1",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback2": {
                            "/": {
                                "get": {
                                    "summary": "Callback2",
                                    "operationId": "callback2__get",
                                    "parameters": [
                                        {
                                            "name": "level2",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level2",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback5": {
                            "/": {
                                "get": {
                                    "summary": "Callback5",
                                    "operationId": "callback5__get",
                                    "parameters": [
                                        {
                                            "name": "level5",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level5",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                    },
                    "deprecated": True,
                }
            },
            "/level1/level2/default5": {
                "get": {
                    "tags": ["level1a", "level1b", "level2a", "level2b"],
                    "summary": "Path5 Default Router4 Default",
                    "operationId": "path5_default_router4_default_level1_level2_default5_get",
                    "parameters": [
                        {
                            "required": True,
                            "schema": {"title": "Level5", "type": "string"},
                            "name": "level5",
                            "in": "query",
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/x-level-2": {"schema": {}}},
                        },
                        "400": {"description": "Client error level 0"},
                        "401": {"description": "Client error level 1"},
                        "402": {"description": "Client error level 2"},
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
                        "500": {"description": "Server error level 0"},
                        "501": {"description": "Server error level 1"},
                        "502": {"description": "Server error level 2"},
                    },
                    "callbacks": {
                        "callback0": {
                            "/": {
                                "get": {
                                    "summary": "Callback0",
                                    "operationId": "callback0__get",
                                    "parameters": [
                                        {
                                            "name": "level0",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level0",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback1": {
                            "/": {
                                "get": {
                                    "summary": "Callback1",
                                    "operationId": "callback1__get",
                                    "parameters": [
                                        {
                                            "name": "level1",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level1",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback2": {
                            "/": {
                                "get": {
                                    "summary": "Callback2",
                                    "operationId": "callback2__get",
                                    "parameters": [
                                        {
                                            "name": "level2",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level2",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                    },
                    "deprecated": True,
                }
            },
            "/level1/override3": {
                "get": {
                    "tags": ["level1a", "level1b", "path3a", "path3b"],
                    "summary": "Path3 Override Router2 Default",
                    "operationId": "path3_override_router2_default_level1_override3_get",
                    "parameters": [
                        {
                            "required": True,
                            "schema": {"title": "Level3", "type": "string"},
                            "name": "level3",
                            "in": "query",
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/x-level-3": {"schema": {}}},
                        },
                        "400": {"description": "Client error level 0"},
                        "401": {"description": "Client error level 1"},
                        "403": {"description": "Client error level 3"},
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
                        "500": {"description": "Server error level 0"},
                        "501": {"description": "Server error level 1"},
                        "503": {"description": "Server error level 3"},
                    },
                    "callbacks": {
                        "callback0": {
                            "/": {
                                "get": {
                                    "summary": "Callback0",
                                    "operationId": "callback0__get",
                                    "parameters": [
                                        {
                                            "name": "level0",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level0",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback1": {
                            "/": {
                                "get": {
                                    "summary": "Callback1",
                                    "operationId": "callback1__get",
                                    "parameters": [
                                        {
                                            "name": "level1",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level1",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback3": {
                            "/": {
                                "get": {
                                    "summary": "Callback3",
                                    "operationId": "callback3__get",
                                    "parameters": [
                                        {
                                            "name": "level3",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level3",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                    },
                    "deprecated": True,
                }
            },
            "/level1/default3": {
                "get": {
                    "tags": ["level1a", "level1b"],
                    "summary": "Path3 Default Router2 Default",
                    "operationId": "path3_default_router2_default_level1_default3_get",
                    "parameters": [
                        {
                            "required": True,
                            "schema": {"title": "Level3", "type": "string"},
                            "name": "level3",
                            "in": "query",
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/x-level-1": {"schema": {}}},
                        },
                        "400": {"description": "Client error level 0"},
                        "401": {"description": "Client error level 1"},
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
                        "500": {"description": "Server error level 0"},
                        "501": {"description": "Server error level 1"},
                    },
                    "callbacks": {
                        "callback0": {
                            "/": {
                                "get": {
                                    "summary": "Callback0",
                                    "operationId": "callback0__get",
                                    "parameters": [
                                        {
                                            "name": "level0",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level0",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback1": {
                            "/": {
                                "get": {
                                    "summary": "Callback1",
                                    "operationId": "callback1__get",
                                    "parameters": [
                                        {
                                            "name": "level1",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level1",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                    },
                }
            },
            "/level1/level3/level4/override5": {
                "get": {
                    "tags": [
                        "level1a",
                        "level1b",
                        "level3a",
                        "level3b",
                        "level4a",
                        "level4b",
                        "path5a",
                        "path5b",
                    ],
                    "summary": "Path5 Override Router4 Override",
                    "operationId": "path5_override_router4_override_level1_level3_level4_override5_get",
                    "parameters": [
                        {
                            "required": True,
                            "schema": {"title": "Level5", "type": "string"},
                            "name": "level5",
                            "in": "query",
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/x-level-5": {"schema": {}}},
                        },
                        "400": {"description": "Client error level 0"},
                        "401": {"description": "Client error level 1"},
                        "403": {"description": "Client error level 3"},
                        "404": {"description": "Client error level 4"},
                        "405": {"description": "Client error level 5"},
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
                        "500": {"description": "Server error level 0"},
                        "501": {"description": "Server error level 1"},
                        "503": {"description": "Server error level 3"},
                        "504": {"description": "Server error level 4"},
                        "505": {"description": "Server error level 5"},
                    },
                    "callbacks": {
                        "callback0": {
                            "/": {
                                "get": {
                                    "summary": "Callback0",
                                    "operationId": "callback0__get",
                                    "parameters": [
                                        {
                                            "name": "level0",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level0",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback1": {
                            "/": {
                                "get": {
                                    "summary": "Callback1",
                                    "operationId": "callback1__get",
                                    "parameters": [
                                        {
                                            "name": "level1",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level1",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback3": {
                            "/": {
                                "get": {
                                    "summary": "Callback3",
                                    "operationId": "callback3__get",
                                    "parameters": [
                                        {
                                            "name": "level3",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level3",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback4": {
                            "/": {
                                "get": {
                                    "summary": "Callback4",
                                    "operationId": "callback4__get",
                                    "parameters": [
                                        {
                                            "name": "level4",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level4",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback5": {
                            "/": {
                                "get": {
                                    "summary": "Callback5",
                                    "operationId": "callback5__get",
                                    "parameters": [
                                        {
                                            "name": "level5",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level5",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                    },
                    "deprecated": True,
                }
            },
            "/level1/level3/level4/default5": {
                "get": {
                    "tags": [
                        "level1a",
                        "level1b",
                        "level3a",
                        "level3b",
                        "level4a",
                        "level4b",
                    ],
                    "summary": "Path5 Default Router4 Override",
                    "operationId": "path5_default_router4_override_level1_level3_level4_default5_get",
                    "parameters": [
                        {
                            "required": True,
                            "schema": {"title": "Level5", "type": "string"},
                            "name": "level5",
                            "in": "query",
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/x-level-4": {"schema": {}}},
                        },
                        "400": {"description": "Client error level 0"},
                        "401": {"description": "Client error level 1"},
                        "403": {"description": "Client error level 3"},
                        "404": {"description": "Client error level 4"},
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
                        "500": {"description": "Server error level 0"},
                        "501": {"description": "Server error level 1"},
                        "503": {"description": "Server error level 3"},
                        "504": {"description": "Server error level 4"},
                    },
                    "callbacks": {
                        "callback0": {
                            "/": {
                                "get": {
                                    "summary": "Callback0",
                                    "operationId": "callback0__get",
                                    "parameters": [
                                        {
                                            "name": "level0",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level0",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback1": {
                            "/": {
                                "get": {
                                    "summary": "Callback1",
                                    "operationId": "callback1__get",
                                    "parameters": [
                                        {
                                            "name": "level1",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level1",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback3": {
                            "/": {
                                "get": {
                                    "summary": "Callback3",
                                    "operationId": "callback3__get",
                                    "parameters": [
                                        {
                                            "name": "level3",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level3",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback4": {
                            "/": {
                                "get": {
                                    "summary": "Callback4",
                                    "operationId": "callback4__get",
                                    "parameters": [
                                        {
                                            "name": "level4",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level4",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                    },
                    "deprecated": True,
                }
            },
            "/level1/level3/override5": {
                "get": {
                    "tags": [
                        "level1a",
                        "level1b",
                        "level3a",
                        "level3b",
                        "path5a",
                        "path5b",
                    ],
                    "summary": "Path5 Override Router4 Default",
                    "operationId": "path5_override_router4_default_level1_level3_override5_get",
                    "parameters": [
                        {
                            "required": True,
                            "schema": {"title": "Level5", "type": "string"},
                            "name": "level5",
                            "in": "query",
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/x-level-5": {"schema": {}}},
                        },
                        "400": {"description": "Client error level 0"},
                        "401": {"description": "Client error level 1"},
                        "403": {"description": "Client error level 3"},
                        "405": {"description": "Client error level 5"},
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
                        "500": {"description": "Server error level 0"},
                        "501": {"description": "Server error level 1"},
                        "503": {"description": "Server error level 3"},
                        "505": {"description": "Server error level 5"},
                    },
                    "callbacks": {
                        "callback0": {
                            "/": {
                                "get": {
                                    "summary": "Callback0",
                                    "operationId": "callback0__get",
                                    "parameters": [
                                        {
                                            "name": "level0",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level0",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback1": {
                            "/": {
                                "get": {
                                    "summary": "Callback1",
                                    "operationId": "callback1__get",
                                    "parameters": [
                                        {
                                            "name": "level1",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level1",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback3": {
                            "/": {
                                "get": {
                                    "summary": "Callback3",
                                    "operationId": "callback3__get",
                                    "parameters": [
                                        {
                                            "name": "level3",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level3",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback5": {
                            "/": {
                                "get": {
                                    "summary": "Callback5",
                                    "operationId": "callback5__get",
                                    "parameters": [
                                        {
                                            "name": "level5",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level5",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                    },
                    "deprecated": True,
                }
            },
            "/level1/level3/default5": {
                "get": {
                    "tags": ["level1a", "level1b", "level3a", "level3b"],
                    "summary": "Path5 Default Router4 Default",
                    "operationId": "path5_default_router4_default_level1_level3_default5_get",
                    "parameters": [
                        {
                            "required": True,
                            "schema": {"title": "Level5", "type": "string"},
                            "name": "level5",
                            "in": "query",
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/x-level-3": {"schema": {}}},
                        },
                        "400": {"description": "Client error level 0"},
                        "401": {"description": "Client error level 1"},
                        "403": {"description": "Client error level 3"},
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
                        "500": {"description": "Server error level 0"},
                        "501": {"description": "Server error level 1"},
                        "503": {"description": "Server error level 3"},
                    },
                    "callbacks": {
                        "callback0": {
                            "/": {
                                "get": {
                                    "summary": "Callback0",
                                    "operationId": "callback0__get",
                                    "parameters": [
                                        {
                                            "name": "level0",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level0",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback1": {
                            "/": {
                                "get": {
                                    "summary": "Callback1",
                                    "operationId": "callback1__get",
                                    "parameters": [
                                        {
                                            "name": "level1",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level1",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback3": {
                            "/": {
                                "get": {
                                    "summary": "Callback3",
                                    "operationId": "callback3__get",
                                    "parameters": [
                                        {
                                            "name": "level3",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level3",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                    },
                }
            },
            "/level1/level4/override5": {
                "get": {
                    "tags": [
                        "level1a",
                        "level1b",
                        "level4a",
                        "level4b",
                        "path5a",
                        "path5b",
                    ],
                    "summary": "Path5 Override Router4 Override",
                    "operationId": "path5_override_router4_override_level1_level4_override5_get",
                    "parameters": [
                        {
                            "required": True,
                            "schema": {"title": "Level5", "type": "string"},
                            "name": "level5",
                            "in": "query",
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/x-level-5": {"schema": {}}},
                        },
                        "400": {"description": "Client error level 0"},
                        "401": {"description": "Client error level 1"},
                        "404": {"description": "Client error level 4"},
                        "405": {"description": "Client error level 5"},
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
                        "500": {"description": "Server error level 0"},
                        "501": {"description": "Server error level 1"},
                        "504": {"description": "Server error level 4"},
                        "505": {"description": "Server error level 5"},
                    },
                    "callbacks": {
                        "callback0": {
                            "/": {
                                "get": {
                                    "summary": "Callback0",
                                    "operationId": "callback0__get",
                                    "parameters": [
                                        {
                                            "name": "level0",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level0",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback1": {
                            "/": {
                                "get": {
                                    "summary": "Callback1",
                                    "operationId": "callback1__get",
                                    "parameters": [
                                        {
                                            "name": "level1",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level1",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback4": {
                            "/": {
                                "get": {
                                    "summary": "Callback4",
                                    "operationId": "callback4__get",
                                    "parameters": [
                                        {
                                            "name": "level4",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level4",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback5": {
                            "/": {
                                "get": {
                                    "summary": "Callback5",
                                    "operationId": "callback5__get",
                                    "parameters": [
                                        {
                                            "name": "level5",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level5",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                    },
                    "deprecated": True,
                }
            },
            "/level1/level4/default5": {
                "get": {
                    "tags": ["level1a", "level1b", "level4a", "level4b"],
                    "summary": "Path5 Default Router4 Override",
                    "operationId": "path5_default_router4_override_level1_level4_default5_get",
                    "parameters": [
                        {
                            "required": True,
                            "schema": {"title": "Level5", "type": "string"},
                            "name": "level5",
                            "in": "query",
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/x-level-4": {"schema": {}}},
                        },
                        "400": {"description": "Client error level 0"},
                        "401": {"description": "Client error level 1"},
                        "404": {"description": "Client error level 4"},
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
                        "500": {"description": "Server error level 0"},
                        "501": {"description": "Server error level 1"},
                        "504": {"description": "Server error level 4"},
                    },
                    "callbacks": {
                        "callback0": {
                            "/": {
                                "get": {
                                    "summary": "Callback0",
                                    "operationId": "callback0__get",
                                    "parameters": [
                                        {
                                            "name": "level0",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level0",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback1": {
                            "/": {
                                "get": {
                                    "summary": "Callback1",
                                    "operationId": "callback1__get",
                                    "parameters": [
                                        {
                                            "name": "level1",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level1",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback4": {
                            "/": {
                                "get": {
                                    "summary": "Callback4",
                                    "operationId": "callback4__get",
                                    "parameters": [
                                        {
                                            "name": "level4",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level4",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                    },
                    "deprecated": True,
                }
            },
            "/level1/override5": {
                "get": {
                    "tags": ["level1a", "level1b", "path5a", "path5b"],
                    "summary": "Path5 Override Router4 Default",
                    "operationId": "path5_override_router4_default_level1_override5_get",
                    "parameters": [
                        {
                            "required": True,
                            "schema": {"title": "Level5", "type": "string"},
                            "name": "level5",
                            "in": "query",
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/x-level-5": {"schema": {}}},
                        },
                        "400": {"description": "Client error level 0"},
                        "401": {"description": "Client error level 1"},
                        "405": {"description": "Client error level 5"},
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
                        "500": {"description": "Server error level 0"},
                        "501": {"description": "Server error level 1"},
                        "505": {"description": "Server error level 5"},
                    },
                    "callbacks": {
                        "callback0": {
                            "/": {
                                "get": {
                                    "summary": "Callback0",
                                    "operationId": "callback0__get",
                                    "parameters": [
                                        {
                                            "name": "level0",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level0",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback1": {
                            "/": {
                                "get": {
                                    "summary": "Callback1",
                                    "operationId": "callback1__get",
                                    "parameters": [
                                        {
                                            "name": "level1",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level1",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback5": {
                            "/": {
                                "get": {
                                    "summary": "Callback5",
                                    "operationId": "callback5__get",
                                    "parameters": [
                                        {
                                            "name": "level5",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level5",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                    },
                    "deprecated": True,
                }
            },
            "/level1/default5": {
                "get": {
                    "tags": ["level1a", "level1b"],
                    "summary": "Path5 Default Router4 Default",
                    "operationId": "path5_default_router4_default_level1_default5_get",
                    "parameters": [
                        {
                            "required": True,
                            "schema": {"title": "Level5", "type": "string"},
                            "name": "level5",
                            "in": "query",
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/x-level-1": {"schema": {}}},
                        },
                        "400": {"description": "Client error level 0"},
                        "401": {"description": "Client error level 1"},
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
                        "500": {"description": "Server error level 0"},
                        "501": {"description": "Server error level 1"},
                    },
                    "callbacks": {
                        "callback0": {
                            "/": {
                                "get": {
                                    "summary": "Callback0",
                                    "operationId": "callback0__get",
                                    "parameters": [
                                        {
                                            "name": "level0",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level0",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback1": {
                            "/": {
                                "get": {
                                    "summary": "Callback1",
                                    "operationId": "callback1__get",
                                    "parameters": [
                                        {
                                            "name": "level1",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level1",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                    },
                }
            },
            "/level2/override3": {
                "get": {
                    "tags": ["level2a", "level2b", "path3a", "path3b"],
                    "summary": "Path3 Override Router2 Override",
                    "operationId": "path3_override_router2_override_level2_override3_get",
                    "parameters": [
                        {
                            "required": True,
                            "schema": {"title": "Level3", "type": "string"},
                            "name": "level3",
                            "in": "query",
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/x-level-3": {"schema": {}}},
                        },
                        "400": {"description": "Client error level 0"},
                        "402": {"description": "Client error level 2"},
                        "403": {"description": "Client error level 3"},
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
                        "500": {"description": "Server error level 0"},
                        "502": {"description": "Server error level 2"},
                        "503": {"description": "Server error level 3"},
                    },
                    "callbacks": {
                        "callback0": {
                            "/": {
                                "get": {
                                    "summary": "Callback0",
                                    "operationId": "callback0__get",
                                    "parameters": [
                                        {
                                            "name": "level0",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level0",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback2": {
                            "/": {
                                "get": {
                                    "summary": "Callback2",
                                    "operationId": "callback2__get",
                                    "parameters": [
                                        {
                                            "name": "level2",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level2",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback3": {
                            "/": {
                                "get": {
                                    "summary": "Callback3",
                                    "operationId": "callback3__get",
                                    "parameters": [
                                        {
                                            "name": "level3",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level3",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                    },
                    "deprecated": True,
                }
            },
            "/level2/default3": {
                "get": {
                    "tags": ["level2a", "level2b"],
                    "summary": "Path3 Default Router2 Override",
                    "operationId": "path3_default_router2_override_level2_default3_get",
                    "parameters": [
                        {
                            "required": True,
                            "schema": {"title": "Level3", "type": "string"},
                            "name": "level3",
                            "in": "query",
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/x-level-2": {"schema": {}}},
                        },
                        "400": {"description": "Client error level 0"},
                        "402": {"description": "Client error level 2"},
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
                        "500": {"description": "Server error level 0"},
                        "502": {"description": "Server error level 2"},
                    },
                    "callbacks": {
                        "callback0": {
                            "/": {
                                "get": {
                                    "summary": "Callback0",
                                    "operationId": "callback0__get",
                                    "parameters": [
                                        {
                                            "name": "level0",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level0",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback2": {
                            "/": {
                                "get": {
                                    "summary": "Callback2",
                                    "operationId": "callback2__get",
                                    "parameters": [
                                        {
                                            "name": "level2",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level2",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                    },
                    "deprecated": True,
                }
            },
            "/level2/level3/level4/override5": {
                "get": {
                    "tags": [
                        "level2a",
                        "level2b",
                        "level3a",
                        "level3b",
                        "level4a",
                        "level4b",
                        "path5a",
                        "path5b",
                    ],
                    "summary": "Path5 Override Router4 Override",
                    "operationId": "path5_override_router4_override_level2_level3_level4_override5_get",
                    "parameters": [
                        {
                            "required": True,
                            "schema": {"title": "Level5", "type": "string"},
                            "name": "level5",
                            "in": "query",
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/x-level-5": {"schema": {}}},
                        },
                        "400": {"description": "Client error level 0"},
                        "402": {"description": "Client error level 2"},
                        "403": {"description": "Client error level 3"},
                        "404": {"description": "Client error level 4"},
                        "405": {"description": "Client error level 5"},
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
                        "500": {"description": "Server error level 0"},
                        "502": {"description": "Server error level 2"},
                        "503": {"description": "Server error level 3"},
                        "504": {"description": "Server error level 4"},
                        "505": {"description": "Server error level 5"},
                    },
                    "callbacks": {
                        "callback0": {
                            "/": {
                                "get": {
                                    "summary": "Callback0",
                                    "operationId": "callback0__get",
                                    "parameters": [
                                        {
                                            "name": "level0",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level0",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback2": {
                            "/": {
                                "get": {
                                    "summary": "Callback2",
                                    "operationId": "callback2__get",
                                    "parameters": [
                                        {
                                            "name": "level2",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level2",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback3": {
                            "/": {
                                "get": {
                                    "summary": "Callback3",
                                    "operationId": "callback3__get",
                                    "parameters": [
                                        {
                                            "name": "level3",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level3",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback4": {
                            "/": {
                                "get": {
                                    "summary": "Callback4",
                                    "operationId": "callback4__get",
                                    "parameters": [
                                        {
                                            "name": "level4",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level4",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback5": {
                            "/": {
                                "get": {
                                    "summary": "Callback5",
                                    "operationId": "callback5__get",
                                    "parameters": [
                                        {
                                            "name": "level5",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level5",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                    },
                    "deprecated": True,
                }
            },
            "/level2/level3/level4/default5": {
                "get": {
                    "tags": [
                        "level2a",
                        "level2b",
                        "level3a",
                        "level3b",
                        "level4a",
                        "level4b",
                    ],
                    "summary": "Path5 Default Router4 Override",
                    "operationId": "path5_default_router4_override_level2_level3_level4_default5_get",
                    "parameters": [
                        {
                            "required": True,
                            "schema": {"title": "Level5", "type": "string"},
                            "name": "level5",
                            "in": "query",
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/x-level-4": {"schema": {}}},
                        },
                        "400": {"description": "Client error level 0"},
                        "402": {"description": "Client error level 2"},
                        "403": {"description": "Client error level 3"},
                        "404": {"description": "Client error level 4"},
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
                        "500": {"description": "Server error level 0"},
                        "502": {"description": "Server error level 2"},
                        "503": {"description": "Server error level 3"},
                        "504": {"description": "Server error level 4"},
                    },
                    "callbacks": {
                        "callback0": {
                            "/": {
                                "get": {
                                    "summary": "Callback0",
                                    "operationId": "callback0__get",
                                    "parameters": [
                                        {
                                            "name": "level0",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level0",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback2": {
                            "/": {
                                "get": {
                                    "summary": "Callback2",
                                    "operationId": "callback2__get",
                                    "parameters": [
                                        {
                                            "name": "level2",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level2",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback3": {
                            "/": {
                                "get": {
                                    "summary": "Callback3",
                                    "operationId": "callback3__get",
                                    "parameters": [
                                        {
                                            "name": "level3",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level3",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback4": {
                            "/": {
                                "get": {
                                    "summary": "Callback4",
                                    "operationId": "callback4__get",
                                    "parameters": [
                                        {
                                            "name": "level4",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level4",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                    },
                    "deprecated": True,
                }
            },
            "/level2/level3/override5": {
                "get": {
                    "tags": [
                        "level2a",
                        "level2b",
                        "level3a",
                        "level3b",
                        "path5a",
                        "path5b",
                    ],
                    "summary": "Path5 Override Router4 Default",
                    "operationId": "path5_override_router4_default_level2_level3_override5_get",
                    "parameters": [
                        {
                            "required": True,
                            "schema": {"title": "Level5", "type": "string"},
                            "name": "level5",
                            "in": "query",
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/x-level-5": {"schema": {}}},
                        },
                        "400": {"description": "Client error level 0"},
                        "402": {"description": "Client error level 2"},
                        "403": {"description": "Client error level 3"},
                        "405": {"description": "Client error level 5"},
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
                        "500": {"description": "Server error level 0"},
                        "502": {"description": "Server error level 2"},
                        "503": {"description": "Server error level 3"},
                        "505": {"description": "Server error level 5"},
                    },
                    "callbacks": {
                        "callback0": {
                            "/": {
                                "get": {
                                    "summary": "Callback0",
                                    "operationId": "callback0__get",
                                    "parameters": [
                                        {
                                            "name": "level0",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level0",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback2": {
                            "/": {
                                "get": {
                                    "summary": "Callback2",
                                    "operationId": "callback2__get",
                                    "parameters": [
                                        {
                                            "name": "level2",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level2",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback3": {
                            "/": {
                                "get": {
                                    "summary": "Callback3",
                                    "operationId": "callback3__get",
                                    "parameters": [
                                        {
                                            "name": "level3",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level3",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback5": {
                            "/": {
                                "get": {
                                    "summary": "Callback5",
                                    "operationId": "callback5__get",
                                    "parameters": [
                                        {
                                            "name": "level5",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level5",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                    },
                    "deprecated": True,
                }
            },
            "/level2/level3/default5": {
                "get": {
                    "tags": ["level2a", "level2b", "level3a", "level3b"],
                    "summary": "Path5 Default Router4 Default",
                    "operationId": "path5_default_router4_default_level2_level3_default5_get",
                    "parameters": [
                        {
                            "required": True,
                            "schema": {"title": "Level5", "type": "string"},
                            "name": "level5",
                            "in": "query",
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/x-level-3": {"schema": {}}},
                        },
                        "400": {"description": "Client error level 0"},
                        "402": {"description": "Client error level 2"},
                        "403": {"description": "Client error level 3"},
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
                        "500": {"description": "Server error level 0"},
                        "502": {"description": "Server error level 2"},
                        "503": {"description": "Server error level 3"},
                    },
                    "callbacks": {
                        "callback0": {
                            "/": {
                                "get": {
                                    "summary": "Callback0",
                                    "operationId": "callback0__get",
                                    "parameters": [
                                        {
                                            "name": "level0",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level0",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback2": {
                            "/": {
                                "get": {
                                    "summary": "Callback2",
                                    "operationId": "callback2__get",
                                    "parameters": [
                                        {
                                            "name": "level2",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level2",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback3": {
                            "/": {
                                "get": {
                                    "summary": "Callback3",
                                    "operationId": "callback3__get",
                                    "parameters": [
                                        {
                                            "name": "level3",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level3",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                    },
                    "deprecated": True,
                }
            },
            "/level2/level4/override5": {
                "get": {
                    "tags": [
                        "level2a",
                        "level2b",
                        "level4a",
                        "level4b",
                        "path5a",
                        "path5b",
                    ],
                    "summary": "Path5 Override Router4 Override",
                    "operationId": "path5_override_router4_override_level2_level4_override5_get",
                    "parameters": [
                        {
                            "required": True,
                            "schema": {"title": "Level5", "type": "string"},
                            "name": "level5",
                            "in": "query",
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/x-level-5": {"schema": {}}},
                        },
                        "400": {"description": "Client error level 0"},
                        "402": {"description": "Client error level 2"},
                        "404": {"description": "Client error level 4"},
                        "405": {"description": "Client error level 5"},
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
                        "500": {"description": "Server error level 0"},
                        "502": {"description": "Server error level 2"},
                        "504": {"description": "Server error level 4"},
                        "505": {"description": "Server error level 5"},
                    },
                    "callbacks": {
                        "callback0": {
                            "/": {
                                "get": {
                                    "summary": "Callback0",
                                    "operationId": "callback0__get",
                                    "parameters": [
                                        {
                                            "name": "level0",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level0",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback2": {
                            "/": {
                                "get": {
                                    "summary": "Callback2",
                                    "operationId": "callback2__get",
                                    "parameters": [
                                        {
                                            "name": "level2",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level2",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback4": {
                            "/": {
                                "get": {
                                    "summary": "Callback4",
                                    "operationId": "callback4__get",
                                    "parameters": [
                                        {
                                            "name": "level4",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level4",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback5": {
                            "/": {
                                "get": {
                                    "summary": "Callback5",
                                    "operationId": "callback5__get",
                                    "parameters": [
                                        {
                                            "name": "level5",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level5",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                    },
                    "deprecated": True,
                }
            },
            "/level2/level4/default5": {
                "get": {
                    "tags": ["level2a", "level2b", "level4a", "level4b"],
                    "summary": "Path5 Default Router4 Override",
                    "operationId": "path5_default_router4_override_level2_level4_default5_get",
                    "parameters": [
                        {
                            "required": True,
                            "schema": {"title": "Level5", "type": "string"},
                            "name": "level5",
                            "in": "query",
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/x-level-4": {"schema": {}}},
                        },
                        "400": {"description": "Client error level 0"},
                        "402": {"description": "Client error level 2"},
                        "404": {"description": "Client error level 4"},
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
                        "500": {"description": "Server error level 0"},
                        "502": {"description": "Server error level 2"},
                        "504": {"description": "Server error level 4"},
                    },
                    "callbacks": {
                        "callback0": {
                            "/": {
                                "get": {
                                    "summary": "Callback0",
                                    "operationId": "callback0__get",
                                    "parameters": [
                                        {
                                            "name": "level0",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level0",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback2": {
                            "/": {
                                "get": {
                                    "summary": "Callback2",
                                    "operationId": "callback2__get",
                                    "parameters": [
                                        {
                                            "name": "level2",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level2",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback4": {
                            "/": {
                                "get": {
                                    "summary": "Callback4",
                                    "operationId": "callback4__get",
                                    "parameters": [
                                        {
                                            "name": "level4",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level4",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                    },
                    "deprecated": True,
                }
            },
            "/level2/override5": {
                "get": {
                    "tags": ["level2a", "level2b", "path5a", "path5b"],
                    "summary": "Path5 Override Router4 Default",
                    "operationId": "path5_override_router4_default_level2_override5_get",
                    "parameters": [
                        {
                            "required": True,
                            "schema": {"title": "Level5", "type": "string"},
                            "name": "level5",
                            "in": "query",
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/x-level-5": {"schema": {}}},
                        },
                        "400": {"description": "Client error level 0"},
                        "402": {"description": "Client error level 2"},
                        "405": {"description": "Client error level 5"},
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
                        "500": {"description": "Server error level 0"},
                        "502": {"description": "Server error level 2"},
                        "505": {"description": "Server error level 5"},
                    },
                    "callbacks": {
                        "callback0": {
                            "/": {
                                "get": {
                                    "summary": "Callback0",
                                    "operationId": "callback0__get",
                                    "parameters": [
                                        {
                                            "name": "level0",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level0",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback2": {
                            "/": {
                                "get": {
                                    "summary": "Callback2",
                                    "operationId": "callback2__get",
                                    "parameters": [
                                        {
                                            "name": "level2",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level2",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback5": {
                            "/": {
                                "get": {
                                    "summary": "Callback5",
                                    "operationId": "callback5__get",
                                    "parameters": [
                                        {
                                            "name": "level5",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level5",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                    },
                    "deprecated": True,
                }
            },
            "/level2/default5": {
                "get": {
                    "tags": ["level2a", "level2b"],
                    "summary": "Path5 Default Router4 Default",
                    "operationId": "path5_default_router4_default_level2_default5_get",
                    "parameters": [
                        {
                            "required": True,
                            "schema": {"title": "Level5", "type": "string"},
                            "name": "level5",
                            "in": "query",
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/x-level-2": {"schema": {}}},
                        },
                        "400": {"description": "Client error level 0"},
                        "402": {"description": "Client error level 2"},
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
                        "500": {"description": "Server error level 0"},
                        "502": {"description": "Server error level 2"},
                    },
                    "callbacks": {
                        "callback0": {
                            "/": {
                                "get": {
                                    "summary": "Callback0",
                                    "operationId": "callback0__get",
                                    "parameters": [
                                        {
                                            "name": "level0",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level0",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback2": {
                            "/": {
                                "get": {
                                    "summary": "Callback2",
                                    "operationId": "callback2__get",
                                    "parameters": [
                                        {
                                            "name": "level2",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level2",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                    },
                    "deprecated": True,
                }
            },
            "/override3": {
                "get": {
                    "tags": ["path3a", "path3b"],
                    "summary": "Path3 Override Router2 Default",
                    "operationId": "path3_override_router2_default_override3_get",
                    "parameters": [
                        {
                            "required": True,
                            "schema": {"title": "Level3", "type": "string"},
                            "name": "level3",
                            "in": "query",
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/x-level-3": {"schema": {}}},
                        },
                        "400": {"description": "Client error level 0"},
                        "403": {"description": "Client error level 3"},
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
                        "500": {"description": "Server error level 0"},
                        "503": {"description": "Server error level 3"},
                    },
                    "callbacks": {
                        "callback0": {
                            "/": {
                                "get": {
                                    "summary": "Callback0",
                                    "operationId": "callback0__get",
                                    "parameters": [
                                        {
                                            "name": "level0",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level0",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback3": {
                            "/": {
                                "get": {
                                    "summary": "Callback3",
                                    "operationId": "callback3__get",
                                    "parameters": [
                                        {
                                            "name": "level3",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level3",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                    },
                    "deprecated": True,
                }
            },
            "/default3": {
                "get": {
                    "summary": "Path3 Default Router2 Default",
                    "operationId": "path3_default_router2_default_default3_get",
                    "parameters": [
                        {
                            "required": True,
                            "schema": {"title": "Level3", "type": "string"},
                            "name": "level3",
                            "in": "query",
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/x-level-0": {"schema": {}}},
                        },
                        "400": {"description": "Client error level 0"},
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
                        "500": {"description": "Server error level 0"},
                    },
                    "callbacks": {
                        "callback0": {
                            "/": {
                                "get": {
                                    "summary": "Callback0",
                                    "operationId": "callback0__get",
                                    "parameters": [
                                        {
                                            "name": "level0",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level0",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
            "/level3/level4/override5": {
                "get": {
                    "tags": [
                        "level3a",
                        "level3b",
                        "level4a",
                        "level4b",
                        "path5a",
                        "path5b",
                    ],
                    "summary": "Path5 Override Router4 Override",
                    "operationId": "path5_override_router4_override_level3_level4_override5_get",
                    "parameters": [
                        {
                            "required": True,
                            "schema": {"title": "Level5", "type": "string"},
                            "name": "level5",
                            "in": "query",
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/x-level-5": {"schema": {}}},
                        },
                        "400": {"description": "Client error level 0"},
                        "403": {"description": "Client error level 3"},
                        "404": {"description": "Client error level 4"},
                        "405": {"description": "Client error level 5"},
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
                        "500": {"description": "Server error level 0"},
                        "503": {"description": "Server error level 3"},
                        "504": {"description": "Server error level 4"},
                        "505": {"description": "Server error level 5"},
                    },
                    "callbacks": {
                        "callback0": {
                            "/": {
                                "get": {
                                    "summary": "Callback0",
                                    "operationId": "callback0__get",
                                    "parameters": [
                                        {
                                            "name": "level0",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level0",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback3": {
                            "/": {
                                "get": {
                                    "summary": "Callback3",
                                    "operationId": "callback3__get",
                                    "parameters": [
                                        {
                                            "name": "level3",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level3",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback4": {
                            "/": {
                                "get": {
                                    "summary": "Callback4",
                                    "operationId": "callback4__get",
                                    "parameters": [
                                        {
                                            "name": "level4",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level4",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback5": {
                            "/": {
                                "get": {
                                    "summary": "Callback5",
                                    "operationId": "callback5__get",
                                    "parameters": [
                                        {
                                            "name": "level5",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level5",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                    },
                    "deprecated": True,
                }
            },
            "/level3/level4/default5": {
                "get": {
                    "tags": ["level3a", "level3b", "level4a", "level4b"],
                    "summary": "Path5 Default Router4 Override",
                    "operationId": "path5_default_router4_override_level3_level4_default5_get",
                    "parameters": [
                        {
                            "required": True,
                            "schema": {"title": "Level5", "type": "string"},
                            "name": "level5",
                            "in": "query",
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/x-level-4": {"schema": {}}},
                        },
                        "400": {"description": "Client error level 0"},
                        "403": {"description": "Client error level 3"},
                        "404": {"description": "Client error level 4"},
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
                        "500": {"description": "Server error level 0"},
                        "503": {"description": "Server error level 3"},
                        "504": {"description": "Server error level 4"},
                    },
                    "callbacks": {
                        "callback0": {
                            "/": {
                                "get": {
                                    "summary": "Callback0",
                                    "operationId": "callback0__get",
                                    "parameters": [
                                        {
                                            "name": "level0",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level0",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback3": {
                            "/": {
                                "get": {
                                    "summary": "Callback3",
                                    "operationId": "callback3__get",
                                    "parameters": [
                                        {
                                            "name": "level3",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level3",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback4": {
                            "/": {
                                "get": {
                                    "summary": "Callback4",
                                    "operationId": "callback4__get",
                                    "parameters": [
                                        {
                                            "name": "level4",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level4",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                    },
                    "deprecated": True,
                }
            },
            "/level3/override5": {
                "get": {
                    "tags": ["level3a", "level3b", "path5a", "path5b"],
                    "summary": "Path5 Override Router4 Default",
                    "operationId": "path5_override_router4_default_level3_override5_get",
                    "parameters": [
                        {
                            "required": True,
                            "schema": {"title": "Level5", "type": "string"},
                            "name": "level5",
                            "in": "query",
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/x-level-5": {"schema": {}}},
                        },
                        "400": {"description": "Client error level 0"},
                        "403": {"description": "Client error level 3"},
                        "405": {"description": "Client error level 5"},
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
                        "500": {"description": "Server error level 0"},
                        "503": {"description": "Server error level 3"},
                        "505": {"description": "Server error level 5"},
                    },
                    "callbacks": {
                        "callback0": {
                            "/": {
                                "get": {
                                    "summary": "Callback0",
                                    "operationId": "callback0__get",
                                    "parameters": [
                                        {
                                            "name": "level0",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level0",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback3": {
                            "/": {
                                "get": {
                                    "summary": "Callback3",
                                    "operationId": "callback3__get",
                                    "parameters": [
                                        {
                                            "name": "level3",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level3",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback5": {
                            "/": {
                                "get": {
                                    "summary": "Callback5",
                                    "operationId": "callback5__get",
                                    "parameters": [
                                        {
                                            "name": "level5",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level5",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                    },
                    "deprecated": True,
                }
            },
            "/level3/default5": {
                "get": {
                    "tags": ["level3a", "level3b"],
                    "summary": "Path5 Default Router4 Default",
                    "operationId": "path5_default_router4_default_level3_default5_get",
                    "parameters": [
                        {
                            "required": True,
                            "schema": {"title": "Level5", "type": "string"},
                            "name": "level5",
                            "in": "query",
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/x-level-3": {"schema": {}}},
                        },
                        "400": {"description": "Client error level 0"},
                        "403": {"description": "Client error level 3"},
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
                        "500": {"description": "Server error level 0"},
                        "503": {"description": "Server error level 3"},
                    },
                    "callbacks": {
                        "callback0": {
                            "/": {
                                "get": {
                                    "summary": "Callback0",
                                    "operationId": "callback0__get",
                                    "parameters": [
                                        {
                                            "name": "level0",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level0",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback3": {
                            "/": {
                                "get": {
                                    "summary": "Callback3",
                                    "operationId": "callback3__get",
                                    "parameters": [
                                        {
                                            "name": "level3",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level3",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                    },
                }
            },
            "/level4/override5": {
                "get": {
                    "tags": ["level4a", "level4b", "path5a", "path5b"],
                    "summary": "Path5 Override Router4 Override",
                    "operationId": "path5_override_router4_override_level4_override5_get",
                    "parameters": [
                        {
                            "required": True,
                            "schema": {"title": "Level5", "type": "string"},
                            "name": "level5",
                            "in": "query",
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/x-level-5": {"schema": {}}},
                        },
                        "400": {"description": "Client error level 0"},
                        "404": {"description": "Client error level 4"},
                        "405": {"description": "Client error level 5"},
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
                        "500": {"description": "Server error level 0"},
                        "504": {"description": "Server error level 4"},
                        "505": {"description": "Server error level 5"},
                    },
                    "callbacks": {
                        "callback0": {
                            "/": {
                                "get": {
                                    "summary": "Callback0",
                                    "operationId": "callback0__get",
                                    "parameters": [
                                        {
                                            "name": "level0",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level0",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback4": {
                            "/": {
                                "get": {
                                    "summary": "Callback4",
                                    "operationId": "callback4__get",
                                    "parameters": [
                                        {
                                            "name": "level4",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level4",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback5": {
                            "/": {
                                "get": {
                                    "summary": "Callback5",
                                    "operationId": "callback5__get",
                                    "parameters": [
                                        {
                                            "name": "level5",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level5",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                    },
                    "deprecated": True,
                }
            },
            "/level4/default5": {
                "get": {
                    "tags": ["level4a", "level4b"],
                    "summary": "Path5 Default Router4 Override",
                    "operationId": "path5_default_router4_override_level4_default5_get",
                    "parameters": [
                        {
                            "required": True,
                            "schema": {"title": "Level5", "type": "string"},
                            "name": "level5",
                            "in": "query",
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/x-level-4": {"schema": {}}},
                        },
                        "400": {"description": "Client error level 0"},
                        "404": {"description": "Client error level 4"},
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
                        "500": {"description": "Server error level 0"},
                        "504": {"description": "Server error level 4"},
                    },
                    "callbacks": {
                        "callback0": {
                            "/": {
                                "get": {
                                    "summary": "Callback0",
                                    "operationId": "callback0__get",
                                    "parameters": [
                                        {
                                            "name": "level0",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level0",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback4": {
                            "/": {
                                "get": {
                                    "summary": "Callback4",
                                    "operationId": "callback4__get",
                                    "parameters": [
                                        {
                                            "name": "level4",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level4",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                    },
                    "deprecated": True,
                }
            },
            "/override5": {
                "get": {
                    "tags": ["path5a", "path5b"],
                    "summary": "Path5 Override Router4 Default",
                    "operationId": "path5_override_router4_default_override5_get",
                    "parameters": [
                        {
                            "required": True,
                            "schema": {"title": "Level5", "type": "string"},
                            "name": "level5",
                            "in": "query",
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/x-level-5": {"schema": {}}},
                        },
                        "400": {"description": "Client error level 0"},
                        "405": {"description": "Client error level 5"},
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
                        "500": {"description": "Server error level 0"},
                        "505": {"description": "Server error level 5"},
                    },
                    "callbacks": {
                        "callback0": {
                            "/": {
                                "get": {
                                    "summary": "Callback0",
                                    "operationId": "callback0__get",
                                    "parameters": [
                                        {
                                            "name": "level0",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level0",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                        "callback5": {
                            "/": {
                                "get": {
                                    "summary": "Callback5",
                                    "operationId": "callback5__get",
                                    "parameters": [
                                        {
                                            "name": "level5",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level5",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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
                        },
                    },
                    "deprecated": True,
                }
            },
            "/default5": {
                "get": {
                    "summary": "Path5 Default Router4 Default",
                    "operationId": "path5_default_router4_default_default5_get",
                    "parameters": [
                        {
                            "required": True,
                            "schema": {"title": "Level5", "type": "string"},
                            "name": "level5",
                            "in": "query",
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/x-level-0": {"schema": {}}},
                        },
                        "400": {"description": "Client error level 0"},
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
                        "500": {"description": "Server error level 0"},
                    },
                    "callbacks": {
                        "callback0": {
                            "/": {
                                "get": {
                                    "summary": "Callback0",
                                    "operationId": "callback0__get",
                                    "parameters": [
                                        {
                                            "name": "level0",
                                            "in": "query",
                                            "required": True,
                                            "schema": {
                                                "title": "Level0",
                                                "type": "string",
                                            },
                                        }
                                    ],
                                    "responses": {
                                        "200": {
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
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