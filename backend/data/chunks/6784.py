    def echo(
        data: str = Body(..., examples=["123"]),
    ) -> str:
        if data == "error":
            raise MyError(data={"details": "error"})
        else:
            return data