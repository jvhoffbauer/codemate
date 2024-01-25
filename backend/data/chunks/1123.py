        def __get_pydantic_core_schema__(
            cls, source: Type[Any], handler: Callable[[Any], CoreSchema]
        ) -> CoreSchema:
            return with_info_plain_validator_function(cls._validate)