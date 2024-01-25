def Default(value: _TDefaultType) -> _TDefaultType:
    """
    You shouldn't use this function directly.

    It's used internally to recognize when a default value has been overwritten, even
    if the overridden default value was truthy.
    """
    return _DefaultPlaceholder(value)  # type: ignore