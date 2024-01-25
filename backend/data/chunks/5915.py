    def register_crud(
        self,
        schema_list: Type[SchemaListT] = None,
        schema_filter: Type[SchemaFilterT] = None,
        schema_create: Type[SchemaCreateT] = None,
        schema_read: Type[
            SchemaReadT
        ] = None,  # default is None, means not use read route.
        schema_update: Type[SchemaUpdateT] = None,
        list_per_page_max: int = None,
        depends_list: List[Depends] = None,
        depends_read: List[Depends] = None,
        depends_create: List[Depends] = None,
        depends_update: List[Depends] = None,
        depends_delete: List[Depends] = None,
    ) -> "BaseCrud":
        self.schema_list = schema_list or self.schema_list or self._create_schema_list()
        self.schema_filter = (
            schema_filter or self.schema_filter or self._create_schema_filter()
        )
        self.schema_create = (
            schema_create or self.schema_create or self._create_schema_create()
        )
        self.schema_read = schema_read or self.schema_read or self._create_schema_read()
        self.schema_update = (
            schema_update or self.schema_update or self._create_schema_update()
        )
        self.list_per_page_max = list_per_page_max or self.list_per_page_max
        self.paginator = Paginator(perPageMax=self.list_per_page_max)
        self.router.add_api_route(
            "/list",
            self.route_list,
            methods=["POST"],
            response_model=BaseApiOut[ItemListSchema[self.schema_list]],
            dependencies=depends_list,
            name=CrudEnum.list,
        )
        if self.schema_read:
            self.router.add_api_route(
                "/item/{item_id}",
                self.route_read,
                methods=["GET"],
                response_model=BaseApiOut[
                    Union[self.schema_read, List[self.schema_read]]
                ],
                dependencies=depends_read,
                name=CrudEnum.read,
            )
        self.router.add_api_route(
            "/item",
            self.route_create,
            methods=["POST"],
            response_model=BaseApiOut[Union[int, self.schema_model]],
            dependencies=depends_create,
            name=CrudEnum.create,
        )
        self.router.add_api_route(
            "/item/{item_id}",
            self.route_update,
            methods=["PUT"],
            response_model=BaseApiOut[int],
            dependencies=depends_update,
            name=CrudEnum.update,
        )
        self.router.add_api_route(
            "/item/{item_id}",
            self.route_delete,
            methods=["DELETE"],
            response_model=BaseApiOut[int],
            dependencies=depends_delete,
            name=CrudEnum.delete,
        )
        return self