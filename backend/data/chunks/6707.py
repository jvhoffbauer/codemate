@component_name(f"_Response")
class JsonRpcResponse(BaseModel):
    jsonrpc: Literal["2.0"] = Field("2.0", json_schema_extra={"example": "2.0"})
    id: Union[StrictStr, int] = Field(None, json_schema_extra={"example": 0})
    result: dict

    model_config = ConfigDict(
        extra="forbid", json_schema_serialization_defaults_required=True
    )