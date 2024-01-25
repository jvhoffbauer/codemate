@component_name(f"_Request")
class JsonRpcRequest(BaseModel):
    jsonrpc: Literal["2.0"] = Field("2.0", json_schema_extra={"example": "2.0"})
    id: Union[StrictStr, int] = Field(None, json_schema_extra={"example": 0})
    method: StrictStr
    params: dict = Field(default_factory=dict)

    model_config = ConfigDict(extra="forbid")