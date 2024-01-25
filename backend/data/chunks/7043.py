    @ep.method(errors=[FirstError, SecondError])
    def my_method__with_mergeable_errors() -> None:
        return None