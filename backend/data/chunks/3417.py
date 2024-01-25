        @app.get("/")
        async def get2(foo: Annotated[int, Depends(dep)] = Depends(dep)):
            pass  # pragma: nocover