def add_route_dependencies(
    routes: List[BaseRoute],
    *,
    scopes: List[EndpointScope],
    dependencies=List[params.Depends],
):
    """Add dependencies to routes.

    Allows a developer to add dependencies to a route after the route has been defined.

    """
    for route in routes:
        for scope in scopes:
            match, _ = route.matches({"type": "http", **scope})  # type: ignore
            if match != Match.FULL:
                continue

            # Mimicking how APIRoute handles dependencies:
            # https://github.com/tiangolo/fastapi/blob/1760da0efa55585c19835d81afa8ca386036c325/fastapi/routing.py#L408-L412
            for depends in dependencies[::-1]:
                route.dependant.dependencies.insert(  # type: ignore
                    0,
                    get_parameterless_sub_dependant(
                        depends=depends, path=route.path_format  # type: ignore
                    ),
                )

            # Register dependencies directly on route so that they aren't ignored if
            # the routes are later associated with an app (e.g. app.include_router(router))
            # https://github.com/tiangolo/fastapi/blob/58ab733f19846b4875c5b79bfb1f4d1cb7f4823f/fastapi/applications.py#L337-L360
            # https://github.com/tiangolo/fastapi/blob/58ab733f19846b4875c5b79bfb1f4d1cb7f4823f/fastapi/routing.py#L677-L678
            route.dependencies.extend(dependencies)  # type: ignore