- Creates a new item with name 'Foo' using POST request to '/items/' endpoint
- Verifies that server returns HTTP status code 200 and expected JSON response containing just the 'name' field (assuming no description was provided in the request body)