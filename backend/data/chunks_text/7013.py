- Updates an existing item with new data provided in `item_in`.
- Requires authentication using FastAPI's dependency injection system.
- Checks whether the authenticated user has sufficient permissions to update the item based on its owner ID. Raises a custom error message if necessary.