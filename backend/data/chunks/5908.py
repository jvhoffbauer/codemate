    def get_router(self) -> APIRouter:
        if self.router is None:
            if self.router_prefix is None:
                self.router_prefix = f"/{self.__class__.__name__}"
            self.router = APIRouter(
                prefix=self.router_prefix, tags=[self.router_prefix[1:]]
            )
        if self.router_permission_depend is not None:
            self.router.dependencies.insert(0, Depends(self.router_permission_depend))
        return self.router