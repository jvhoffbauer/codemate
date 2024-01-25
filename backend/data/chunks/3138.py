    @router.get("/hello/")
    def hello_page() -> str:
        return "Hello, World!"