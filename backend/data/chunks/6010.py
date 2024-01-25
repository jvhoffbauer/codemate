    def register_router(self):
        self.router.add_api_route(
            self.page_path,
            self.route_page,
            methods=["GET"],
            dependencies=[Depends(self.page_permission_depend)],
            include_in_schema=False,
            response_class=HTMLResponse,
            **self.page_route_kwargs,
        )
        self.router.add_api_route(
            self.page_path,
            self.route_page,
            methods=["POST"],
            dependencies=[Depends(self.page_permission_depend)],
            response_model=BaseAmisApiOut,
            include_in_schema=(self.page_parser_mode == "json"),
            **self.page_route_kwargs,
        )
        return self