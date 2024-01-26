- Tests the `GET /api/v1/home` endpoint with an authenticated user (represented by `superuser_token_headers`) using PyTest's async fixture `AsyncClient`.
- Asserts that the response status is 200 and the body contains a specific string ("Hello World!") in JSON format.