- Tests that passing a non-matching query parameter value to `item-query` raises a validation error with a specific message and location in the URL path. - Uses Pytest's `needs_py310` fixture to ensure compatibility with Python 3.10 or higher. - Imports `IsDict` from `asgiref.typed` for type hinting of JSON responses.