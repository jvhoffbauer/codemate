def ep(ep_path):
    class Entrypoint(jsonrpc.Entrypoint):
        async def handle_exception(self, exc):
            if isinstance(exc, MyErrorToUnhandledException):
                raise MyUnhandledException("My unhandled exception")
            elif isinstance(exc, MyErrorToConvert):
                raise MyConvertedError
            else:
                raise NotImplementedError

    ep = Entrypoint(ep_path)

    @ep.method()
    def unhandled_exception() -> int:
        raise MyErrorToUnhandledException()

    @ep.method()
    def convert_error() -> int:
        raise MyErrorToConvert()

    return ep