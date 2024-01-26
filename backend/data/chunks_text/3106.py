- Defines a function `query_example_examples()` that takes an optional argument `data`.
- The `Query` decorator is used to define the type hint and provide defaults, examples, and overriding behavior for the `data` parameter.
- If no value is provided for `data`, it will be set to `None` by default. However, if a string value of 'query_overridden' is passed as the input, this value will override the default.
- Two additional examples ('query1', 'query2') are also defined using the `examples` attribute of the `Query` decorator. These can be accessed through the OpenAPI documentation or other tools that support Pydantic schema validation.