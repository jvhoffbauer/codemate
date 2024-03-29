- This function is a PUT request handler for updating an existing item with ID `item_id`.
- The updated item data is passed in as a JSON object (`item`) and encoded using `jsonable_encoder()`.
- The updated item dictionary is stored directly into the global `items` dictionary under its original key (`item_id`).
- The updated item dictionary is returned to the client as the response body.