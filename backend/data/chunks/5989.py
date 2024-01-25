    def register_router(self):
        self.pk_admin.router.add_api_route(
            self.path + "/{item_id}",
            self.route_delete,
            methods=["DELETE"],
            response_model=BaseApiOut[int],
            name=f"{self.link_model.name}_Delete",
        )

        self.pk_admin.router.add_api_route(
            self.path + "/{item_id}",
            self.route_create,
            methods=["POST"],
            response_model=BaseApiOut[int],
            name=f"{self.link_model.name}_Create",
        )

        return self