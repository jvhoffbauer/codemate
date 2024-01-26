- Defines a function `query_example` with one positional argument `data`.
- The argument is annotated as a union type of string or None using Pydantic's `Union` and `Query` decorators.
- If no value is provided for this parameter during API request, it will be set to its default value (None) specified in the `default` keyword argument of `Query`. Alternatively, if a value is provided, it should conform to the `example` constraint specified in the same decorator.