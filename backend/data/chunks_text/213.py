- Creates a new hero with name 'Deadpond' and secret name 'Dive Wilson' using POST request to '/heroes/' endpoint. - Verifies that the status code of the response is 200, indicating successful creation. - Extracts the JSON response body and asserts that the expected fields are present and have correct values. - Asserts that the 'age' field is null since it was not provided in the request body. - Asserts that an ID for the newly created hero has been generated by the server and included in the response.