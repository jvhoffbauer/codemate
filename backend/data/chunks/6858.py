def ep(ep):
    @ep.method()
    def probe1(
        data: List[Balance],
    ) -> List[Balance]:
        return data

    @ep.method()
    def probe2(
        data: List[Balance],
    ) -> List[Balance]:
        return data

    return ep