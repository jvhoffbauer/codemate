    def add_method_route(
        self,
        func: Union[FunctionType, Coroutine],
        *,
        name: str = None,
        **kwargs,
    ) -> None:
        name = name or func.__name__
        tags = list(self.entrypoint_route.tags)
        tags.extend(kwargs.pop("tags", ()))
        route = self.method_route_class(
            self,
            self.entrypoint_route.path + "/" + name,
            func,
            name=name,
            request_class=self.request_class,
            tags=tags,
            **kwargs,
        )
        self.routes.append(route)