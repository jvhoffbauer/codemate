- Defines a function `get_config_value()` that takes three arguments: `model`, `parameter`, and an optional `default`.
- The `model` argument can be either an instance of SQLModel or its type (class).
- Inside the function, it retrieves the value for the specified `parameter` from the `model_config` dictionary of the given `model`. If the key is not found in the dictionary, it returns the provided `default` instead.