- Retrieves a list of all model fields that should be included in requests to an API endpoint based on a given `Dependant`.
- First gets a flattened version of the dependent using `get_flat_dependant()`, with repetitions skipped.
- Combines the path parameters, query parameters, header parameters, and cookie parameters from the flattened dependent into a single list of model fields.