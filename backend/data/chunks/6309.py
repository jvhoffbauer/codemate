    @site.register_admin
    class TmpAdmin(admin.RouterAdmin):
        router_prefix = "/router"

        def register_router(self):
            @self.router.get("/hello")
            def hello():
                return {"username": "hello"}