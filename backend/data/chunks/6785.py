def test_basic(ep, app, app_client, openapi_compatible):
    # noinspection PyUnusedLocal
    @ep.method()
    def probe(
        data: List[str] = Body(..., examples=["111", "222"]),
        amount: int = Body(..., gt=5, examples=[10]),
    ) -> List[int]:
        del data, amount
        return [1, 2, 3]

    app.bind_entrypoint(ep)

    resp = app_client.get("/openapi.json")
    assert resp.json() == openapi_compatible(
        {
            "components": {
                "schemas": {
                    "InternalError": {
                        "properties": {
                            "code": {
                                "default": -32603,
                                "example": -32603,
                                "title": "Code",
                                "type": "integer",
                            },
                            "message": {
                                "default": "Internal error",
                                "example": "Internal error",
                                "title": "Message",
                                "type": "string",
                            },
                        },
                        "title": "InternalError",
                        "type": "object",
                    },
                    "InvalidParams": {
                        "properties": {
                            "code": {
                                "default": -32602,
                                "example": -32602,
                                "title": "Code",
                                "type": "integer",
                            },
                            "data": {
                                "anyOf": [
                                    {
                                        "$ref": "#/components/schemas/_ErrorData[_Error]",
                                    },
                                    {"type": "null"},
                                ]
                            },
                            "message": {
                                "default": "Invalid params",
                                "example": "Invalid params",
                                "title": "Message",
                                "type": "string",
                            },
                        },
                        "title": "InvalidParams",
                        "type": "object",
                    },
                    "InvalidRequest": {
                        "properties": {
                            "code": {
                                "default": -32600,
                                "example": -32600,
                                "title": "Code",
                                "type": "integer",
                            },
                            "data": {
                                "anyOf": [
                                    {
                                        "$ref": "#/components/schemas/_ErrorData[_Error]",
                                    },
                                    {"type": "null"},
                                ]
                            },
                            "message": {
                                "default": "Invalid Request",
                                "example": "Invalid Request",
                                "title": "Message",
                                "type": "string",
                            },
                        },
                        "title": "InvalidRequest",
                        "type": "object",
                    },
                    "MethodNotFound": {
                        "properties": {
                            "code": {
                                "default": -32601,
                                "example": -32601,
                                "title": "Code",
                                "type": "integer",
                            },
                            "message": {
                                "default": "Method not found",
                                "example": "Method not found",
                                "title": "Message",
                                "type": "string",
                            },
                        },
                        "title": "MethodNotFound",
                        "type": "object",
                    },
                    "ParseError": {
                        "properties": {
                            "code": {
                                "default": -32700,
                                "example": -32700,
                                "title": "Code",
                                "type": "integer",
                            },
                            "message": {
                                "default": "Parse error",
                                "example": "Parse error",
                                "title": "Message",
                                "type": "string",
                            },
                        },
                        "title": "ParseError",
                        "type": "object",
                    },
                    "_Error": {
                        "properties": {
                            "ctx": {
                                "title": "Ctx",
                                "anyOf": [{"type": "object"}, {"type": "null"}],
                            },
                            "loc": {
                                "items": {
                                    "anyOf": [
                                        {"type": "string"},
                                        {"type": "integer"},
                                    ]
                                },
                                "title": "Loc",
                                "type": "array",
                            },
                            "msg": {
                                "title": "Msg",
                                "type": "string",
                            },
                            "type": {
                                "title": "Type",
                                "type": "string",
                            },
                        },
                        "required": ["loc", "msg", "type"],
                        "title": "_Error",
                        "type": "object",
                    },
                    "_ErrorData[_Error]": {
                        "properties": {
                            "errors": {
                                "anyOf": [
                                    {
                                        "items": {
                                            "$ref": "#/components/schemas/_Error"
                                        },
                                        "type": "array",
                                    },
                                    {"type": "null"},
                                ],
                                "title": "Errors",
                            },
                        },
                        "title": "_ErrorData[_Error]",
                        "type": "object",
                    },
                    "_ErrorResponse[InternalError]": {
                        "additionalProperties": False,
                        "properties": {
                            "error": {
                                "$ref": "#/components/schemas/InternalError",
                            },
                            "id": {
                                "anyOf": [
                                    {
                                        "type": "string",
                                    },
                                    {
                                        "type": "integer",
                                    },
                                ],
                                "example": 0,
                                "title": "Id",
                            },
                            "jsonrpc": {
                                "const": "2.0",
                                "default": "2.0",
                                "example": "2.0",
                                "title": "Jsonrpc",
                            },
                        },
                        "required": ["error"],
                        "title": "_ErrorResponse[InternalError]",
                        "type": "object",
                    },
                    "_ErrorResponse[InvalidParams]": {
                        "additionalProperties": False,
                        "properties": {
                            "error": {
                                "$ref": "#/components/schemas/InvalidParams",
                            },
                            "id": {
                                "anyOf": [
                                    {
                                        "type": "string",
                                    },
                                    {
                                        "type": "integer",
                                    },
                                ],
                                "example": 0,
                                "title": "Id",
                            },
                            "jsonrpc": {
                                "const": "2.0",
                                "default": "2.0",
                                "example": "2.0",
                                "title": "Jsonrpc",
                            },
                        },
                        "required": ["error"],
                        "title": "_ErrorResponse[InvalidParams]",
                        "type": "object",
                    },
                    "_ErrorResponse[InvalidRequest]": {
                        "additionalProperties": False,
                        "properties": {
                            "error": {
                                "$ref": "#/components/schemas/InvalidRequest",
                            },
                            "id": {
                                "anyOf": [
                                    {
                                        "type": "string",
                                    },
                                    {
                                        "type": "integer",
                                    },
                                ],
                                "example": 0,
                                "title": "Id",
                            },
                            "jsonrpc": {
                                "const": "2.0",
                                "default": "2.0",
                                "example": "2.0",
                                "title": "Jsonrpc",
                            },
                        },
                        "required": ["error"],
                        "title": "_ErrorResponse[InvalidRequest]",
                        "type": "object",
                    },
                    "_ErrorResponse[MethodNotFound]": {
                        "additionalProperties": False,
                        "properties": {
                            "error": {
                                "$ref": "#/components/schemas/MethodNotFound",
                            },
                            "id": {
                                "anyOf": [
                                    {
                                        "type": "string",
                                    },
                                    {
                                        "type": "integer",
                                    },
                                ],
                                "example": 0,
                                "title": "Id",
                            },
                            "jsonrpc": {
                                "const": "2.0",
                                "default": "2.0",
                                "example": "2.0",
                                "title": "Jsonrpc",
                            },
                        },
                        "required": ["error"],
                        "title": "_ErrorResponse[MethodNotFound]",
                        "type": "object",
                    },
                    "_ErrorResponse[ParseError]": {
                        "additionalProperties": False,
                        "properties": {
                            "error": {
                                "$ref": "#/components/schemas/ParseError",
                            },
                            "id": {
                                "anyOf": [
                                    {
                                        "type": "string",
                                    },
                                    {
                                        "type": "integer",
                                    },
                                ],
                                "example": 0,
                                "title": "Id",
                            },
                            "jsonrpc": {
                                "const": "2.0",
                                "default": "2.0",
                                "example": "2.0",
                                "title": "Jsonrpc",
                            },
                        },
                        "required": ["error"],
                        "title": "_ErrorResponse[ParseError]",
                        "type": "object",
                    },
                    "_Params[probe]": {
                        "properties": {
                            "amount": {
                                "examples": [10],
                                "exclusiveMinimum": 5.0,
                                "title": "Amount",
                                "type": "integer",
                            },
                            "data": {
                                "examples": ["111", "222"],
                                "items": {
                                    "type": "string",
                                },
                                "title": "Data",
                                "type": "array",
                            },
                        },
                        "required": ["data", "amount"],
                        "title": "_Params[probe]",
                        "type": "object",
                    },
                    "_Request": {
                        "additionalProperties": False,
                        "properties": {
                            "id": {
                                "anyOf": [
                                    {
                                        "type": "string",
                                    },
                                    {
                                        "type": "integer",
                                    },
                                ],
                                "example": 0,
                                "title": "Id",
                            },
                            "jsonrpc": {
                                "const": "2.0",
                                "default": "2.0",
                                "example": "2.0",
                                "title": "Jsonrpc",
                            },
                            "method": {
                                "title": "Method",
                                "type": "string",
                            },
                            "params": {
                                "title": "Params",
                                "type": "object",
                            },
                        },
                        "required": ["method"],
                        "title": "_Request",
                        "type": "object",
                    },
                    "_Request[probe]": {
                        "additionalProperties": False,
                        "properties": {
                            "id": {
                                "anyOf": [
                                    {
                                        "type": "string",
                                    },
                                    {
                                        "type": "integer",
                                    },
                                ],
                                "example": 0,
                                "title": "Id",
                            },
                            "jsonrpc": {
                                "const": "2.0",
                                "default": "2.0",
                                "example": "2.0",
                                "title": "Jsonrpc",
                            },
                            "method": {
                                "default": "probe",
                                "example": "probe",
                                "title": "Method",
                                "type": "string",
                            },
                            "params": {
                                "$ref": "#/components/schemas/_Params[probe]",
                            },
                        },
                        "required": ["params"],
                        "title": "_Request[probe]",
                        "type": "object",
                    },
                    "_Response": {
                        "additionalProperties": False,
                        "properties": {
                            "id": {
                                "anyOf": [
                                    {
                                        "type": "string",
                                    },
                                    {
                                        "type": "integer",
                                    },
                                ],
                                "example": 0,
                                "title": "Id",
                            },
                            "jsonrpc": {
                                "const": "2.0",
                                "default": "2.0",
                                "example": "2.0",
                                "title": "Jsonrpc",
                            },
                            "result": {
                                "title": "Result",
                                "type": "object",
                            },
                        },
                        "required": ["jsonrpc", "id", "result"],
                        "title": "_Response",
                        "type": "object",
                    },
                    "_Response[probe]": {
                        "additionalProperties": False,
                        "properties": {
                            "id": {
                                "anyOf": [
                                    {
                                        "type": "string",
                                    },
                                    {
                                        "type": "integer",
                                    },
                                ],
                                "example": 0,
                                "title": "Id",
                            },
                            "jsonrpc": {
                                "const": "2.0",
                                "default": "2.0",
                                "example": "2.0",
                                "title": "Jsonrpc",
                            },
                            "result": {
                                "items": {
                                    "type": "integer",
                                },
                                "title": "Result",
                                "type": "array",
                            },
                        },
                        "required": ["jsonrpc", "id", "result"],
                        "title": "_Response[probe]",
                        "type": "object",
                    },
                },
            },
            "info": {
                "title": "FastAPI",
                "version": "0.1.0",
            },
            "openapi": "3.0.2",
            "paths": {
                "/api/v1/jsonrpc": {
                    "post": {
                        "operationId": "entrypoint_api_v1_jsonrpc_post",
                        "requestBody": {
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "$ref": "#/components/schemas/_Request",
                                    },
                                },
                            },
                            "required": True,
                        },
                        "responses": {
                            "200": {
                                "content": {
                                    "application/json": {
                                        "schema": {
                                            "$ref": "#/components/schemas/_Response",
                                        },
                                    },
                                },
                                "description": "Successful Response",
                            },
                            "210": {
                                "content": {
                                    "application/json": {
                                        "schema": {
                                            "$ref": "#/components/schemas/_ErrorResponse[InvalidParams]",
                                        },
                                    },
                                },
                                "description": "[-32602] Invalid params\n\nInvalid method parameter(s)",
                            },
                            "211": {
                                "content": {
                                    "application/json": {
                                        "schema": {
                                            "$ref": "#/components/schemas/_ErrorResponse[MethodNotFound]",
                                        },
                                    },
                                },
                                "description": "[-32601] Method not found\n\nThe method does not exist / is not available",
                            },
                            "212": {
                                "content": {
                                    "application/json": {
                                        "schema": {
                                            "$ref": "#/components/schemas/_ErrorResponse[ParseError]",
                                        },
                                    },
                                },
                                "description": "[-32700] Parse error\n\nInvalid JSON was received by the server",
                            },
                            "213": {
                                "content": {
                                    "application/json": {
                                        "schema": {
                                            "$ref": "#/components/schemas/_ErrorResponse[InvalidRequest]",
                                        },
                                    },
                                },
                                "description": "[-32600] Invalid Request\n\nThe JSON sent is not a valid Request object",
                            },
                            "214": {
                                "content": {
                                    "application/json": {
                                        "schema": {
                                            "$ref": "#/components/schemas/_ErrorResponse[InternalError]",
                                        },
                                    },
                                },
                                "description": "[-32603] Internal error\n\nInternal JSON-RPC error",
                            },
                        },
                        "summary": "Entrypoint",
                    },
                },
                "/api/v1/jsonrpc/probe": {
                    "post": {
                        "operationId": "probe_api_v1_jsonrpc_probe_post",
                        "requestBody": {
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "$ref": "#/components/schemas/_Request[probe]",
                                    },
                                },
                            },
                            "required": True,
                        },
                        "responses": {
                            "200": {
                                "content": {
                                    "application/json": {
                                        "schema": {
                                            "$ref": "#/components/schemas/_Response[probe]",
                                        },
                                    },
                                },
                                "description": "Successful Response",
                            },
                        },
                        "summary": "Probe",
                    },
                },
            },
        }
    )