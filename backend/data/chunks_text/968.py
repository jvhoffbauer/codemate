- This function takes two optional arguments `flat_models` and `model_name_map`. It returns a dictionary of JSON schema definitions called `definitions`.
- The `get_model_definitions()` method iterates over all models passed as an argument (stored in `flat_models`) using the `model_process_schema()` helper function to extract their schemas and nested models.
- For each extracted model, its name is looked up in the `model_name_map`, which maps model classes or enum types to human-readable names. These names are used as keys in the final output dictionary `definitions`.
- If a description exists within the model's schema, it gets truncated at the first line break (\f).
- Finally, the resulting dictionary containing all model definitions is returned by the function.