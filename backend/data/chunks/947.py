def match_pydantic_error_url(error_type: str) -> Any:
    from dirty_equals import IsStr

    return IsStr(regex=rf"^https://errors\.pydantic\.dev/.*/v/{error_type}")