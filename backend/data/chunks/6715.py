    @component_name(f"_Response[{name}]", module)
    class _Response(BaseModel):
        jsonrpc: Literal["2.0"] = Field("2.0", json_schema_extra={"example": "2.0"})
        id: Union[StrictStr, int] = Field(None, json_schema_extra={"example": 0})
        result: result_model

        model_config = ConfigDict(
            extra="forbid", json_schema_serialization_defaults_required=True
        )