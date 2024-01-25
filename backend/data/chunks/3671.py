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
                        "501": {"description": "Error 1"},
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/json": {"schema": {}}},
                        },
                    },
                    "summary": "A",
                    "operationId": "a_a_get",
                }
            },
            "/b": {
                "get": {
                    "responses": {
                        "502": {"description": "Error 2"},
                        "4XX": {"description": "Error with range, upper"},
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/json": {"schema": {}}},
                        },
                    },
                    "summary": "B",
                    "operationId": "b_b_get",
                }
            },
            "/c": {
                "get": {
                    "responses": {
                        "400": {"description": "Error with str"},
                        "5XX": {"description": "Error with range, lower"},
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/json": {"schema": {}}},
                        },
                        "default": {"description": "A default response"},
                    },
                    "summary": "C",
                    "operationId": "c_c_get",
                }
            },
            "/d": {
                "get": {
                    "responses": {
                        "400": {"description": "Error with str"},
                        "5XX": {
                            "description": "Server Error",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "$ref": "#/components/schemas/ResponseModel"
                                    }
                                }
                            },
                        },
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/json": {"schema": {}}},
                        },
                        "default": {
                            "description": "Default Response",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "$ref": "#/components/schemas/ResponseModel"
                                    }
                                }
                            },
                        },
                    },
                    "summary": "D",
                    "operationId": "d_d_get",
                }
            },
        },
        "components": {
            "schemas": {
                "ResponseModel": {
                    "title": "ResponseModel",
                    "required": ["message"],
                    "type": "object",
                    "properties": {"message": {"title": "Message", "type": "string"}},
                }
            }
        },
    }