    def probe(
        shared_counter: str = Depends(get_shared_counter),
        common_counter: Tuple[str, int] = Depends(get_common_counter),
    ) -> Tuple[str, str, int]:
        return shared_counter, common_counter[0], common_counter[1]