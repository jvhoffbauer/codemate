        async def read_items(
            q: Annotated[str | None, Form(regex="^fixedquery$")] = None
        ):
            if q:
                return f"Hello {q}"
            else:
                return "Hello World"