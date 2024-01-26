- This function is a FastAPI route with an endpoint `/teams/{team_id}` and returns a Team object in JSON format using the `response_model`.
- The parameter `team_id` is passed as a path variable and converted to an integer using the `int` type hint.
- A dependency injection of the SQLAlchemy session (`Session`) from the `get_session()` function is used to retrieve the corresponding Team object from the database. If the object doesn't exist, a customized HTTP exception is raised with status code 404 and error message "Team not found".