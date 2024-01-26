- Defines a POST endpoint at root URL (/) with `@app.post`.
- Returns a list of `Item` objects as response body using `response_model`, and sets up a custom response for HTTP status code 404 that returns a list of `Message` objects instead.
- Accepts two arguments named `item1` and `item2` both of type `Item` using Pydantic's model validation feature.