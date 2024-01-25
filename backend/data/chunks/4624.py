def test_openapi_schema():
    response = client.get("/openapi.json")
    assert response.status_code == 200, response.text
    assert response.json() == {
        "openapi": "3.1.0",
        "info": {"title": "FastAPI", "version": "0.1.0"},
        "paths": {
            "/items/": {
                "get": {
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/json": {"schema": {}}},
                        }
                    },
                    "tags": ["items"],
                    "summary": "Read Items",
                    "operationId": "read_items_items__get",
                }
            },
            "/users/": {
                "get": {
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/json": {"schema": {}}},
                        }
                    },
                    "tags": ["users"],
                    "summary": "Read Users",
                    "operationId": "read_users_users__get",
                }
            },
            "/elements/": {
                "get": {
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/json": {"schema": {}}},
                        }
                    },
                    "tags": ["items"],
                    "summary": "Read Elements",
                    "operationId": "read_elements_elements__get",
                    "deprecated": True,
                }
            },
        },
    }