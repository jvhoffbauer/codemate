    def get_missing_field_error(loc: Tuple[str, ...]) -> Dict[str, Any]:
        missing_field_error = ErrorWrapper(MissingError(), loc=loc)  # type: ignore[call-arg]
        new_error = ValidationError([missing_field_error], RequestErrorModel)
        return new_error.errors()[0]  # type: ignore[return-value]