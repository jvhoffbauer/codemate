    @ep.method()
    def unhandled_exception() -> int:
        raise MyErrorToUnhandledException()