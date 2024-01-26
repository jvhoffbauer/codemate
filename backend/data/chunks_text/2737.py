- Tests a Flask route that returns a dictionary with extra data using the `ResponseModel` class without annotations
- Uses the Flask client to make a GET request and asserts the status code is 200
- Asserts that the JSON response contains expected keys 'name' and'surname', but also includes additional key(s) due to the lack of annotations in the model definition