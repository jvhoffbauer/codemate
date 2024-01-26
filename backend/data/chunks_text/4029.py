- Sends a POST request to create an item with name 'Foo', price '50.5' (as string), description 'Some Foo' and tax rate of 0.3 using Flask's built-in `TestClient`.
- Asserts that the status code is 200 (OK) and checks if the JSON response matches the expected dictionary containing the provided values for all fields except 'price'. The latter is automatically converted from string to float by Python's JSON library.