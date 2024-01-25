def test_openapi_schema():
    response = client.get("/openapi.json")
    assert response.status_code == 200, response.text
    assert response.json() == {
        "openapi": "3.1.0",
        "info": {"title": "FastAPI", "version": "0.1.0"},
        "paths": {
            "/no_response_model-no_annotation-return_model": {
                "get": {
                    "summary": "No Response Model No Annotation Return Model",
                    "operationId": "no_response_model_no_annotation_return_model_no_response_model_no_annotation_return_model_get",
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/json": {"schema": {}}},
                        }
                    },
                }
            },
            "/no_response_model-no_annotation-return_dict": {
                "get": {
                    "summary": "No Response Model No Annotation Return Dict",
                    "operationId": "no_response_model_no_annotation_return_dict_no_response_model_no_annotation_return_dict_get",
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/json": {"schema": {}}},
                        }
                    },
                }
            },
            "/response_model-no_annotation-return_same_model": {
                "get": {
                    "summary": "Response Model No Annotation Return Same Model",
                    "operationId": "response_model_no_annotation_return_same_model_response_model_no_annotation_return_same_model_get",
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {
                                "application/json": {
                                    "schema": {"$ref": "#/components/schemas/User"}
                                }
                            },
                        }
                    },
                }
            },
            "/response_model-no_annotation-return_exact_dict": {
                "get": {
                    "summary": "Response Model No Annotation Return Exact Dict",
                    "operationId": "response_model_no_annotation_return_exact_dict_response_model_no_annotation_return_exact_dict_get",
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {
                                "application/json": {
                                    "schema": {"$ref": "#/components/schemas/User"}
                                }
                            },
                        }
                    },
                }
            },
            "/response_model-no_annotation-return_invalid_dict": {
                "get": {
                    "summary": "Response Model No Annotation Return Invalid Dict",
                    "operationId": "response_model_no_annotation_return_invalid_dict_response_model_no_annotation_return_invalid_dict_get",
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {
                                "application/json": {
                                    "schema": {"$ref": "#/components/schemas/User"}
                                }
                            },
                        }
                    },
                }
            },
            "/response_model-no_annotation-return_invalid_model": {
                "get": {
                    "summary": "Response Model No Annotation Return Invalid Model",
                    "operationId": "response_model_no_annotation_return_invalid_model_response_model_no_annotation_return_invalid_model_get",
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {
                                "application/json": {
                                    "schema": {"$ref": "#/components/schemas/User"}
                                }
                            },
                        }
                    },
                }
            },
            "/response_model-no_annotation-return_dict_with_extra_data": {
                "get": {
                    "summary": "Response Model No Annotation Return Dict With Extra Data",
                    "operationId": "response_model_no_annotation_return_dict_with_extra_data_response_model_no_annotation_return_dict_with_extra_data_get",
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {
                                "application/json": {
                                    "schema": {"$ref": "#/components/schemas/User"}
                                }
                            },
                        }
                    },
                }
            },
            "/response_model-no_annotation-return_submodel_with_extra_data": {
                "get": {
                    "summary": "Response Model No Annotation Return Submodel With Extra Data",
                    "operationId": "response_model_no_annotation_return_submodel_with_extra_data_response_model_no_annotation_return_submodel_with_extra_data_get",
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {
                                "application/json": {
                                    "schema": {"$ref": "#/components/schemas/User"}
                                }
                            },
                        }
                    },
                }
            },
            "/no_response_model-annotation-return_same_model": {
                "get": {
                    "summary": "No Response Model Annotation Return Same Model",
                    "operationId": "no_response_model_annotation_return_same_model_no_response_model_annotation_return_same_model_get",
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {
                                "application/json": {
                                    "schema": {"$ref": "#/components/schemas/User"}
                                }
                            },
                        }
                    },
                }
            },
            "/no_response_model-annotation-return_exact_dict": {
                "get": {
                    "summary": "No Response Model Annotation Return Exact Dict",
                    "operationId": "no_response_model_annotation_return_exact_dict_no_response_model_annotation_return_exact_dict_get",
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {
                                "application/json": {
                                    "schema": {"$ref": "#/components/schemas/User"}
                                }
                            },
                        }
                    },
                }
            },
            "/no_response_model-annotation-return_invalid_dict": {
                "get": {
                    "summary": "No Response Model Annotation Return Invalid Dict",
                    "operationId": "no_response_model_annotation_return_invalid_dict_no_response_model_annotation_return_invalid_dict_get",
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {
                                "application/json": {
                                    "schema": {"$ref": "#/components/schemas/User"}
                                }
                            },
                        }
                    },
                }
            },
            "/no_response_model-annotation-return_invalid_model": {
                "get": {
                    "summary": "No Response Model Annotation Return Invalid Model",
                    "operationId": "no_response_model_annotation_return_invalid_model_no_response_model_annotation_return_invalid_model_get",
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {
                                "application/json": {
                                    "schema": {"$ref": "#/components/schemas/User"}
                                }
                            },
                        }
                    },
                }
            },
            "/no_response_model-annotation-return_dict_with_extra_data": {
                "get": {
                    "summary": "No Response Model Annotation Return Dict With Extra Data",
                    "operationId": "no_response_model_annotation_return_dict_with_extra_data_no_response_model_annotation_return_dict_with_extra_data_get",
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {
                                "application/json": {
                                    "schema": {"$ref": "#/components/schemas/User"}
                                }
                            },
                        }
                    },
                }
            },
            "/no_response_model-annotation-return_submodel_with_extra_data": {
                "get": {
                    "summary": "No Response Model Annotation Return Submodel With Extra Data",
                    "operationId": "no_response_model_annotation_return_submodel_with_extra_data_no_response_model_annotation_return_submodel_with_extra_data_get",
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {
                                "application/json": {
                                    "schema": {"$ref": "#/components/schemas/User"}
                                }
                            },
                        }
                    },
                }
            },
            "/response_model_none-annotation-return_same_model": {
                "get": {
                    "summary": "Response Model None Annotation Return Same Model",
                    "operationId": "response_model_none_annotation_return_same_model_response_model_none_annotation_return_same_model_get",
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/json": {"schema": {}}},
                        }
                    },
                }
            },
            "/response_model_none-annotation-return_exact_dict": {
                "get": {
                    "summary": "Response Model None Annotation Return Exact Dict",
                    "operationId": "response_model_none_annotation_return_exact_dict_response_model_none_annotation_return_exact_dict_get",
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/json": {"schema": {}}},
                        }
                    },
                }
            },
            "/response_model_none-annotation-return_invalid_dict": {
                "get": {
                    "summary": "Response Model None Annotation Return Invalid Dict",
                    "operationId": "response_model_none_annotation_return_invalid_dict_response_model_none_annotation_return_invalid_dict_get",
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/json": {"schema": {}}},
                        }
                    },
                }
            },
            "/response_model_none-annotation-return_invalid_model": {
                "get": {
                    "summary": "Response Model None Annotation Return Invalid Model",
                    "operationId": "response_model_none_annotation_return_invalid_model_response_model_none_annotation_return_invalid_model_get",
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/json": {"schema": {}}},
                        }
                    },
                }
            },
            "/response_model_none-annotation-return_dict_with_extra_data": {
                "get": {
                    "summary": "Response Model None Annotation Return Dict With Extra Data",
                    "operationId": "response_model_none_annotation_return_dict_with_extra_data_response_model_none_annotation_return_dict_with_extra_data_get",
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/json": {"schema": {}}},
                        }
                    },
                }
            },
            "/response_model_none-annotation-return_submodel_with_extra_data": {
                "get": {
                    "summary": "Response Model None Annotation Return Submodel With Extra Data",
                    "operationId": "response_model_none_annotation_return_submodel_with_extra_data_response_model_none_annotation_return_submodel_with_extra_data_get",
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/json": {"schema": {}}},
                        }
                    },
                }
            },
            "/response_model_model1-annotation_model2-return_same_model": {
                "get": {
                    "summary": "Response Model Model1 Annotation Model2 Return Same Model",
                    "operationId": "response_model_model1_annotation_model2_return_same_model_response_model_model1_annotation_model2_return_same_model_get",
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {
                                "application/json": {
                                    "schema": {"$ref": "#/components/schemas/User"}
                                }
                            },
                        }
                    },
                }
            },
            "/response_model_model1-annotation_model2-return_exact_dict": {
                "get": {
                    "summary": "Response Model Model1 Annotation Model2 Return Exact Dict",
                    "operationId": "response_model_model1_annotation_model2_return_exact_dict_response_model_model1_annotation_model2_return_exact_dict_get",
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {
                                "application/json": {
                                    "schema": {"$ref": "#/components/schemas/User"}
                                }
                            },
                        }
                    },
                }
            },
            "/response_model_model1-annotation_model2-return_invalid_dict": {
                "get": {
                    "summary": "Response Model Model1 Annotation Model2 Return Invalid Dict",
                    "operationId": "response_model_model1_annotation_model2_return_invalid_dict_response_model_model1_annotation_model2_return_invalid_dict_get",
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {
                                "application/json": {
                                    "schema": {"$ref": "#/components/schemas/User"}
                                }
                            },
                        }
                    },
                }
            },
            "/response_model_model1-annotation_model2-return_invalid_model": {
                "get": {
                    "summary": "Response Model Model1 Annotation Model2 Return Invalid Model",
                    "operationId": "response_model_model1_annotation_model2_return_invalid_model_response_model_model1_annotation_model2_return_invalid_model_get",
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {
                                "application/json": {
                                    "schema": {"$ref": "#/components/schemas/User"}
                                }
                            },
                        }
                    },
                }
            },
            "/response_model_model1-annotation_model2-return_dict_with_extra_data": {
                "get": {
                    "summary": "Response Model Model1 Annotation Model2 Return Dict With Extra Data",
                    "operationId": "response_model_model1_annotation_model2_return_dict_with_extra_data_response_model_model1_annotation_model2_return_dict_with_extra_data_get",
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {
                                "application/json": {
                                    "schema": {"$ref": "#/components/schemas/User"}
                                }
                            },
                        }
                    },
                }
            },
            "/response_model_model1-annotation_model2-return_submodel_with_extra_data": {
                "get": {
                    "summary": "Response Model Model1 Annotation Model2 Return Submodel With Extra Data",
                    "operationId": "response_model_model1_annotation_model2_return_submodel_with_extra_data_response_model_model1_annotation_model2_return_submodel_with_extra_data_get",
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {
                                "application/json": {
                                    "schema": {"$ref": "#/components/schemas/User"}
                                }
                            },
                        }
                    },
                }
            },
            "/response_model_filtering_model-annotation_submodel-return_submodel": {
                "get": {
                    "summary": "Response Model Filtering Model Annotation Submodel Return Submodel",
                    "operationId": "response_model_filtering_model_annotation_submodel_return_submodel_response_model_filtering_model_annotation_submodel_return_submodel_get",
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {
                                "application/json": {
                                    "schema": {"$ref": "#/components/schemas/User"}
                                }
                            },
                        }
                    },
                }
            },
            "/response_model_list_of_model-no_annotation": {
                "get": {
                    "summary": "Response Model List Of Model No Annotation",
                    "operationId": "response_model_list_of_model_no_annotation_response_model_list_of_model_no_annotation_get",
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "title": "Response Response Model List Of Model No Annotation Response Model List Of Model No Annotation Get",
                                        "type": "array",
                                        "items": {"$ref": "#/components/schemas/User"},
                                    }
                                }
                            },
                        }
                    },
                }
            },
            "/no_response_model-annotation_list_of_model": {
                "get": {
                    "summary": "No Response Model Annotation List Of Model",
                    "operationId": "no_response_model_annotation_list_of_model_no_response_model_annotation_list_of_model_get",
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "title": "Response No Response Model Annotation List Of Model No Response Model Annotation List Of Model Get",
                                        "type": "array",
                                        "items": {"$ref": "#/components/schemas/User"},
                                    }
                                }
                            },
                        }
                    },
                }
            },
            "/no_response_model-annotation_forward_ref_list_of_model": {
                "get": {
                    "summary": "No Response Model Annotation Forward Ref List Of Model",
                    "operationId": "no_response_model_annotation_forward_ref_list_of_model_no_response_model_annotation_forward_ref_list_of_model_get",
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "title": "Response No Response Model Annotation Forward Ref List Of Model No Response Model Annotation Forward Ref List Of Model Get",
                                        "type": "array",
                                        "items": {"$ref": "#/components/schemas/User"},
                                    }
                                }
                            },
                        }
                    },
                }
            },
            "/response_model_union-no_annotation-return_model1": {
                "get": {
                    "summary": "Response Model Union No Annotation Return Model1",
                    "operationId": "response_model_union_no_annotation_return_model1_response_model_union_no_annotation_return_model1_get",
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "title": "Response Response Model Union No Annotation Return Model1 Response Model Union No Annotation Return Model1 Get",
                                        "anyOf": [
                                            {"$ref": "#/components/schemas/User"},
                                            {"$ref": "#/components/schemas/Item"},
                                        ],
                                    }
                                }
                            },
                        }
                    },
                }
            },
            "/response_model_union-no_annotation-return_model2": {
                "get": {
                    "summary": "Response Model Union No Annotation Return Model2",
                    "operationId": "response_model_union_no_annotation_return_model2_response_model_union_no_annotation_return_model2_get",
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "title": "Response Response Model Union No Annotation Return Model2 Response Model Union No Annotation Return Model2 Get",
                                        "anyOf": [
                                            {"$ref": "#/components/schemas/User"},
                                            {"$ref": "#/components/schemas/Item"},
                                        ],
                                    }
                                }
                            },
                        }
                    },
                }
            },
            "/no_response_model-annotation_union-return_model1": {
                "get": {
                    "summary": "No Response Model Annotation Union Return Model1",
                    "operationId": "no_response_model_annotation_union_return_model1_no_response_model_annotation_union_return_model1_get",
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "title": "Response No Response Model Annotation Union Return Model1 No Response Model Annotation Union Return Model1 Get",
                                        "anyOf": [
                                            {"$ref": "#/components/schemas/User"},
                                            {"$ref": "#/components/schemas/Item"},
                                        ],
                                    }
                                }
                            },
                        }
                    },
                }
            },
            "/no_response_model-annotation_union-return_model2": {
                "get": {
                    "summary": "No Response Model Annotation Union Return Model2",
                    "operationId": "no_response_model_annotation_union_return_model2_no_response_model_annotation_union_return_model2_get",
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "title": "Response No Response Model Annotation Union Return Model2 No Response Model Annotation Union Return Model2 Get",
                                        "anyOf": [
                                            {"$ref": "#/components/schemas/User"},
                                            {"$ref": "#/components/schemas/Item"},
                                        ],
                                    }
                                }
                            },
                        }
                    },
                }
            },
            "/no_response_model-annotation_response_class": {
                "get": {
                    "summary": "No Response Model Annotation Response Class",
                    "operationId": "no_response_model_annotation_response_class_no_response_model_annotation_response_class_get",
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/json": {"schema": {}}},
                        }
                    },
                }
            },
            "/no_response_model-annotation_json_response_class": {
                "get": {
                    "summary": "No Response Model Annotation Json Response Class",
                    "operationId": "no_response_model_annotation_json_response_class_no_response_model_annotation_json_response_class_get",
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/json": {"schema": {}}},
                        }
                    },
                }
            },
        },
        "components": {
            "schemas": {
                "Item": {
                    "title": "Item",
                    "required": ["name", "price"],
                    "type": "object",
                    "properties": {
                        "name": {"title": "Name", "type": "string"},
                        "price": {"title": "Price", "type": "number"},
                    },
                },
                "User": {
                    "title": "User",
                    "required": ["name", "surname"],
                    "type": "object",
                    "properties": {
                        "name": {"title": "Name", "type": "string"},
                        "surname": {"title": "Surname", "type": "string"},
                    },
                },
            }
        },
    }