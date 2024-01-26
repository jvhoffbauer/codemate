- Tests the `test_form_admin_route_submit` function in a Django app using FastAPI's `AsyncClient`.
- Registers an admin class (`TmpAdmin1`) with the admin site (`site`) and retrieves its instance (`ins`).
- Registers the router for the admin site and tests that the initial GET request returns a JSON response containing the correct form configuration.
- Submits the form via POST with some sample data and checks that the expected result is returned as JSON.