    def __init__(
        self,
        *args,
        fastapi_jsonrpc_components_fine_names: bool = True,
        openrpc_url: Optional[str] = "/openrpc.json",
        **kwargs,
    ):
        self.fastapi_jsonrpc_components_fine_names = (
            fastapi_jsonrpc_components_fine_names
        )
        self.openrpc_schema = None
        self.openrpc_url = openrpc_url
        super().__init__(*args, **kwargs)