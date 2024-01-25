    def build_resp_model(cls):
        fields_definition = {
            "code": (
                int,
                Field(cls.CODE, frozen=True, json_schema_extra={"example": cls.CODE}),
            ),
            "message": (
                str,
                Field(
                    cls.MESSAGE, frozen=True, json_schema_extra={"example": cls.MESSAGE}
                ),
            ),
        }

        data_model = cls.get_data_model()
        if data_model is not None:
            data_model_default_value = ...
            if not cls.data_required:
                data_model = Optional[data_model]
                data_model_default_value = None

            fields_definition["data"] = (data_model, data_model_default_value)

        name = cls._component_name or cls.__name__

        _JsonRpcErrorModel = create_model(
            name,
            __base__=(BaseModel,),
            __module__=cls.__module__,
            **fields_definition,
        )
        _JsonRpcErrorModel = component_name(name, cls.__module__)(_JsonRpcErrorModel)

        @component_name(f"_ErrorResponse[{name}]", cls.__module__)
        class _ErrorResponseModel(BaseModel):
            jsonrpc: Literal["2.0"] = Field("2.0", json_schema_extra={"example": "2.0"})
            id: Union[StrictStr, int] = Field(None, json_schema_extra={"example": 0})
            error: _JsonRpcErrorModel

            model_config = ConfigDict(extra="forbid")

        return _ErrorResponseModel