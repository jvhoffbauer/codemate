    def method(
        self,
        **kwargs,
    ) -> Callable:
        def decorator(func: Union[FunctionType, Coroutine]) -> Callable:
            self.add_method_route(
                func,
                **kwargs,
            )
            return func

        return decorator