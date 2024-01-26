- Defines a GET request for an item with ID `item_id`.
- Raises a customized HTTPException (status code 404) when the requested item is not found in the dictionary `items`.
- Includes a custom error header named 'X-Error' in the response.