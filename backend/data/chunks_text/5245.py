- The `__post_init__()` method is called after object initialization to perform additional setup tasks.
- This implementation raises a custom exception (`MissingBands`) when both `bands` and `expression` are empty, indicating that at least one of these attributes should have a value for the object to function properly.