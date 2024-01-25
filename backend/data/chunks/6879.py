    def echo(
        data: str = Body(..., examples=["123"]),
    ) -> str:
        echo_info.history.append(data)
        return data