    def get_common_counter(
        common: str = Body(...),
    ) -> Tuple[str, int]:
        nonlocal _common_counter
        _common_counter += 1
        return common, _common_counter