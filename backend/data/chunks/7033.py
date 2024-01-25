def test_component_schemas(ep, app, app_client):
    class Input(BaseModel):
        x: int = Field(
            ...,
            title="x",
            description="X field",
            gt=1,
            lt=10,
            multiple_of=3,
        )
        y: Optional[str] = Field(
            None,
            alias="Y",
            min_length=1,
            max_length=5,
            pattern=r"^[a-z]{4}$",
        )

        class Config:
            extra = Extra.forbid

    class Output(BaseModel):
        result: List[int] = Field(
            ...,
            min_items=1,
            max_items=10,
        )

    @ep.method()
    def my_method(inp: Input) -> Output:
        return Output(result=[inp.x])

    app.bind_entrypoint(ep)

    resp = app_client.get("/openrpc.json")
    schema = resp.json()

    assert len(schema["methods"]) == 1
    assert schema["methods"][0]["params"] == [
        {
            "name": "inp",
            "schema": {"$ref": "#/components/schemas/Input"},
            "required": True,
        }
    ]
    assert schema["methods"][0]["result"] == {
        "name": "my_method_Result",
        "schema": {"$ref": "#/components/schemas/Output"},
    }

    assert schema["components"]["schemas"] == {
        "Input": {
            "title": "Input",
            "type": "object",
            "properties": {
                "x": {
                    "title": "x",
                    "description": "X field",
                    "exclusiveMinimum": 1,
                    "exclusiveMaximum": 10,
                    "multipleOf": 3,
                    "type": "integer",
                },
                "Y": {
                    "anyOf": [
                        {
                            "maxLength": 5,
                            "minLength": 1,
                            "pattern": "^[a-z]{4}$",
                            "type": "string",
                        },
                        {"type": "null"},
                    ],
                    "default": None,
                    "title": "Y",
                },
            },
            "required": ["x"],
            "additionalProperties": False,
        },
        "Output": {
            "title": "Output",
            "type": "object",
            "properties": {
                "result": {
                    "title": "Result",
                    "minItems": 1,
                    "maxItems": 10,
                    "type": "array",
                    "items": {"type": "integer"},
                }
            },
            "required": ["result"],
        },
    }