        def register_router(self):
            @self.router.get("/hello")
            def hello():
                return {"username": "hello"}