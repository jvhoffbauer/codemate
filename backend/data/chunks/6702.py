        @component_name(f"_ErrorResponse[{name}]", cls.__module__)
        class _ErrorResponseModel(BaseModel):
            jsonrpc: Literal["2.0"] = Field("2.0", json_schema_extra={"example": "2.0"})
            id: Union[StrictStr, int] = Field(None, json_schema_extra={"example": 0})
            error: _JsonRpcErrorModel

            model_config = ConfigDict(extra="forbid")