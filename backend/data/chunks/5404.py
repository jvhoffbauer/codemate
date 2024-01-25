@dataclass  # type: ignore
class BaseTilerFactory(metaclass=abc.ABCMeta):
    """BaseTiler Factory.

    Abstract Base Class which defines most inputs used by dynamic tiler.

    Attributes:
        reader (rio_tiler.io.base.BaseReader): A rio-tiler reader (e.g Reader).
        router (fastapi.APIRouter): Application router to register endpoints to.
        path_dependency (Callable): Endpoint dependency defining `path` to pass to the reader init.
        dataset_dependency (titiler.core.dependencies.DefaultDependency): Endpoint dependency defining dataset overwriting options (e.g nodata).
        layer_dependency (titiler.core.dependencies.DefaultDependency): Endpoint dependency defining dataset indexes/bands/assets options.
        render_dependency (titiler.core.dependencies.DefaultDependency): Endpoint dependency defining image rendering options (e.g add_mask).
        colormap_dependency (Callable): Endpoint dependency defining ColorMap options (e.g colormap_name).
        process_dependency (titiler.core.dependencies.DefaultDependency): Endpoint dependency defining image post-processing options (e.g rescaling, color-formula).
        tms_dependency (Callable): Endpoint dependency defining TileMatrixSet to use.
        reader_dependency (titiler.core.dependencies.DefaultDependency): Endpoint dependency defining BaseReader options.
        environment_dependency (Callable): Endpoint dependency to define GDAL environment at runtime.
        router_prefix (str): prefix where the router will be mounted in the application.
        optional_headers(sequence of titiler.core.resources.enums.OptionalHeader): additional headers to return with the response.

    """

    reader: Type[BaseReader]

    # FastAPI router
    router: APIRouter = field(default_factory=APIRouter)

    # Path Dependency
    path_dependency: Callable[..., Any] = DatasetPathParams

    # Rasterio Dataset Options (nodata, unscale, resampling)
    dataset_dependency: Type[DefaultDependency] = DatasetParams

    # Indexes/Expression Dependencies
    layer_dependency: Type[DefaultDependency] = BidxExprParams

    # Image rendering Dependencies
    render_dependency: Type[DefaultDependency] = ImageRenderingParams
    colormap_dependency: Callable[..., Optional[ColorMapType]] = ColorMapParams

    # Post Processing Dependencies (algorithm)
    process_dependency: Callable[
        ..., Optional[BaseAlgorithm]
    ] = available_algorithms.dependency

    # Reader dependency
    reader_dependency: Type[DefaultDependency] = DefaultDependency

    # GDAL ENV dependency
    environment_dependency: Callable[..., Dict] = field(default=lambda: {})

    # TileMatrixSet dependency
    supported_tms: TileMatrixSets = morecantile_tms
    default_tms: str = "WebMercatorQuad"

    # Router Prefix is needed to find the path for /tile if the TilerFactory.router is mounted
    # with other router (multiple `.../tile` routes).
    # e.g if you mount the route with `/cog` prefix, set router_prefix to cog and
    router_prefix: str = ""

    # add additional headers in response
    optional_headers: List[OptionalHeader] = field(default_factory=list)

    # add dependencies to specific routes
    route_dependencies: List[Tuple[List[EndpointScope], List[DependsFunc]]] = field(
        default_factory=list
    )

    extensions: List[FactoryExtension] = field(default_factory=list)

    def __post_init__(self):
        """Post Init: register route and configure specific options."""
        # Register endpoints
        self.register_routes()

        # Register Extensions
        for ext in self.extensions:
            ext.register(self)

        # Update endpoints dependencies
        for scopes, dependencies in self.route_dependencies:
            self.add_route_dependencies(scopes=scopes, dependencies=dependencies)

    @abc.abstractmethod
    def register_routes(self):
        """Register Tiler Routes."""
        ...

    def url_for(self, request: Request, name: str, **path_params: Any) -> str:
        """Return full url (with prefix) for a specific endpoint."""
        url_path = self.router.url_path_for(name, **path_params)
        base_url = str(request.base_url)
        if self.router_prefix:
            prefix = self.router_prefix.lstrip("/")
            # If we have prefix with custom path param we check and replace them with
            # the path params provided
            if "{" in prefix:
                _, path_format, param_convertors = compile_path(prefix)
                prefix, _ = replace_params(
                    path_format, param_convertors, request.path_params
                )
            base_url += prefix

        url = url_path.make_absolute_url(base_url=base_url)
        return url

    def add_route_dependencies(
        self,
        *,
        scopes: List[EndpointScope],
        dependencies=List[DependsFunc],
    ):
        """Add dependencies to routes.

        Allows a developer to add dependencies to a route after the route has been defined.

        """
        for route in self.router.routes:
            for scope in scopes:
                match, _ = route.matches({"type": "http", **scope})
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