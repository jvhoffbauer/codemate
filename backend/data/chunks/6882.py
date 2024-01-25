    @ep.method()
    def deep_data(
        data: List[DataItem] = Body(...),
    ) -> List[DataItem]:
        return data