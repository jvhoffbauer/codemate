    @contextlib.asynccontextmanager
    async def ep_handle_exception(_ctx: jsonrpc.JsonRpcContext):
        try:
            yield
        except RuntimeError as exc:
            logging.exception(str(exc), exc_info=exc)
            raise _TestError(unique_marker2)