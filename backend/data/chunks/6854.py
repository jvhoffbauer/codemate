    def probe(
        shared_counter: str = Depends(get_shared_counter),
        common_counter: str = Depends(get_common_counter),
    ) -> Tuple[str, str]:
        return shared_counter, common_counter