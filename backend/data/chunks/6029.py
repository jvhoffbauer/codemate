    def register_router(self):
        super().register_router()
        self.router.add_api_route(
            self.form_path,
            self.route_submit,
            methods=["POST"],
            response_model=BaseApiOut[self.schema_submit_out],
            dependencies=[Depends(self.page_permission_depend)],
        )
        if self.form_init:
            self.schema_init_out = self.schema_init_out or create_model_by_model(
                self.schema, f"{self.__class__.__name__}InitOut", set_none=True
            )
            self.router.add_api_route(
                self.form_path,
                self.route_init,
                methods=["GET"],
                response_model=BaseApiOut[self.schema_init_out],
                dependencies=[Depends(self.page_permission_depend)],
            )
        return self