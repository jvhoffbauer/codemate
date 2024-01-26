- Defines an asynchronous function `upsert_item()` that takes three arguments: `item_id`, `name`, and `size`. The first argument is required while the second and third are optional with default values provided by FastAPI's `Body` decorator. - Checks whether the given `item_id` exists in a dictionary called `items`. If it does exist, updates its corresponding fields (i.e., `name` and `size`) using the new values passed to the function. Returns the updated item from the dictionary. - Otherwise, creates a new dictionary for the item with the given `name` and `size` keys initialized with their respective values. Adds this new item to the `items` dictionary and returns a response with status code `201 CREATED` and the newly created item as content.