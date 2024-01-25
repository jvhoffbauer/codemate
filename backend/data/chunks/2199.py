def test_openapi_schema():
    with client:
        response = client.get("/openapi.json")
        assert response.json() == {
            "openapi": "3.1.0",
            "info": {"title": "FastAPI", "version": "0.1.0"},
            "paths": {
                "/invoices/": {
                    "post": {
                        "summary": "Create Invoice",
                        "description": 'Create an invoice.\n\nThis will (let\'s imagine) let the API user (some external developer) create an\ninvoice.\n\nAnd this path operation will:\n\n* Send the invoice to the client.\n* Collect the money from the client.\n* Send a notification back to the API user (the external developer), as a callback.\n    * At this point is that the API will somehow send a POST request to the\n        external API with the notification of the invoice event\n        (e.g. "payment successful").',
                        "operationId": "create_invoice_invoices__post",
                        "parameters": [
                            {
                                "required": False,
                                "schema": IsDict(
                                    {
                                        "title": "Callback Url",
                                        "anyOf": [
                                            {
                                                "type": "string",
                                                "format": "uri",
                                                "minLength": 1,
                                                "maxLength": 2083,
                                            },
                                            {"type": "null"},
                                        ],
                                    }
                                )
                                | IsDict(
                                    # TODO: remove when deprecating Pydantic v1
                                    {
                                        "title": "Callback Url",
                                        "maxLength": 2083,
                                        "minLength": 1,
                                        "type": "string",
                                        "format": "uri",
                                    }
                                ),
                                "name": "callback_url",
                                "in": "query",
                            }
                        ],
                        "requestBody": {
                            "content": {
                                "application/json": {
                                    "schema": {"$ref": "#/components/schemas/Invoice"}
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
                        "callbacks": {
                            "event_callback": {
                                "{$callback_url}/events/{$request.body.title}": {
                                    "get": {
                                        "summary": "Event Callback",
                                        "operationId": "event_callback__callback_url__events___request_body_title__get",
                                        "requestBody": {
                                            "required": True,
                                            "content": {
                                                "application/json": {
                                                    "schema": {
                                                        "$ref": "#/components/schemas/Event"
                                                    }
                                                }
                                            },
                                        },
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
                            "invoice_notification": {
                                "{$callback_url}/invoices/{$request.body.id}": {
                                    "post": {
                                        "summary": "Invoice Notification",
                                        "operationId": "invoice_notification__callback_url__invoices___request_body_id__post",
                                        "requestBody": {
                                            "required": True,
                                            "content": {
                                                "application/json": {
                                                    "schema": {
                                                        "$ref": "#/components/schemas/InvoiceEvent"
                                                    }
                                                }
                                            },
                                        },
                                        "responses": {
                                            "200": {
                                                "description": "Successful Response",
                                                "content": {
                                                    "application/json": {
                                                        "schema": {
                                                            "$ref": "#/components/schemas/InvoiceEventReceived"
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
                            },
                        },
                    }
                }
            },
            "components": {
                "schemas": {
                    "Event": {
                        "title": "Event",
                        "required": ["name", "total"],
                        "type": "object",
                        "properties": {
                            "name": {"title": "Name", "type": "string"},
                            "total": {"title": "Total", "type": "number"},
                        },
                    },
                    "HTTPValidationError": {
                        "title": "HTTPValidationError",
                        "type": "object",
                        "properties": {
                            "detail": {
                                "title": "Detail",
                                "type": "array",
                                "items": {
                                    "$ref": "#/components/schemas/ValidationError"
                                },
                            }
                        },
                    },
                    "Invoice": {
                        "title": "Invoice",
                        "required": ["id", "customer", "total"],
                        "type": "object",
                        "properties": {
                            "id": {"title": "Id", "type": "string"},
                            "title": IsDict(
                                {
                                    "title": "Title",
                                    "anyOf": [{"type": "string"}, {"type": "null"}],
                                }
                            )
                            | IsDict(
                                # TODO: remove when deprecating Pydantic v1
                                {"title": "Title", "type": "string"}
                            ),
                            "customer": {"title": "Customer", "type": "string"},
                            "total": {"title": "Total", "type": "number"},
                        },
                    },
                    "InvoiceEvent": {
                        "title": "InvoiceEvent",
                        "required": ["description", "paid"],
                        "type": "object",
                        "properties": {
                            "description": {"title": "Description", "type": "string"},
                            "paid": {"title": "Paid", "type": "boolean"},
                        },
                    },
                    "InvoiceEventReceived": {
                        "title": "InvoiceEventReceived",
                        "required": ["ok"],
                        "type": "object",
                        "properties": {"ok": {"title": "Ok", "type": "boolean"}},
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