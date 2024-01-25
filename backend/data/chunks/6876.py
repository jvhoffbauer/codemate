def echo(ep, method_request):
    class EchoInfo:
        def __init__(self):
            self.history = []

    echo_info = EchoInfo()

    @ep.method()
    def echo(
        data: str = Body(..., examples=["123"]),
    ) -> str:
        echo_info.history.append(data)
        return data

    @ep.method()
    def no_params() -> str:
        return "123"

    class DataItem(BaseModel):
        inner_data: int

    @ep.method()
    def deep_data(
        data: List[DataItem] = Body(...),
    ) -> List[DataItem]:
        return data

    return echo_info