    @ep.method()
    def convert_error() -> int:
        raise MyErrorToConvert()