    def __init__(
        self,
        path: str,
        *,
        name: str = None,
        errors: List[Type[BaseError]] = None,
        dependencies: Sequence[Depends] = None,
        common_dependencies: Sequence[Depends] = None,
        middlewares: Sequence[JsonRpcMiddleware] = None,
        scheduler_factory: Callable[..., aiojobs.Scheduler] = aiojobs.Scheduler,
        scheduler_kwargs: dict = None,
        request_class: Type[JsonRpcRequest] = JsonRpcRequest,
        **kwargs,
    ) -> None:
        super().__init__(redirect_slashes=False)
        if errors is None:
            errors = list(self.default_errors)
        self.middlewares = middlewares or []
        self.scheduler_factory = scheduler_factory
        self.scheduler_kwargs = scheduler_kwargs
        self.request_class = request_class
        self.scheduler = None
        self.callee_module = inspect.getmodule(inspect.stack()[1][0]).__name__
        self.entrypoint_route = self.entrypoint_route_class(
            self,
            path,
            name=name,
            errors=errors,
            dependencies=dependencies,
            common_dependencies=common_dependencies,
            request_class=request_class,
            **kwargs,
        )
        self.routes.append(self.entrypoint_route)