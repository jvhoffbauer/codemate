            @self.router.get("/hello")
            def hello():
                return {"username": "hello"}