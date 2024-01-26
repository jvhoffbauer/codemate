- This function is a decorator that wraps another function (`cls._validate`) and returns it as a `CoreSchema`.
- The purpose of this decorator is to convert a custom validation function defined in a Pydantic model into a validator function for use by the core schema component of Pydantic.
- It adds metadata to the original validation function using `with_info_plain_validator_function()`, which allows Pydantic's internal error handling mechanism to work correctly when errors occur during validation.