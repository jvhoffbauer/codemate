    @ep.method(errors=[MyError])
    def my_method__with_errors() -> None:
        return None