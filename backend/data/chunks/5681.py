            def route2(
                request: Request, param1: int = Path(...), param2: str = Path(...)
            ):
                """return url."""
                return {"url": self.url_for(request, "route1", param2=param2)}