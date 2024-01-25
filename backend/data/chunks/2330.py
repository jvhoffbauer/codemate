    @app.post("/")
    def foo(foo: Union[str, List[int]]):
        return foo