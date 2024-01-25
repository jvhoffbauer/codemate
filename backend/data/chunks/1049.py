    def get_missing_field_error(loc: Tuple[str, ...]) -> Dict[str, Any]:
        error = ValidationError.from_exception_data(
            "Field required", [{"type": "missing", "loc": loc, "input": {}}]
        ).errors()[0]
        error["input"] = None
        return error  # type: ignore[return-value]