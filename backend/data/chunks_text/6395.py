- Initializes a new instance of the exception class with optional `data` argument. If not provided, an empty dictionary is used as default value. - Copies the original `data` to two attributes (`data` and `raw_data`) after validating it using the `validate_data()` method. - Calls the constructor of the base `Exception` class with specific error codes and messages for this custom exception type.