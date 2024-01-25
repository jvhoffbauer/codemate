            def route1(param1: int = Path(...), param2: str = Path(...)):
                """return param."""
                return {"value": param2}