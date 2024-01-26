- Updates an existing user with new information provided in `user_in`.
- Requires authentication as a superuser using FastAPI's dependency injection system (`Depends`) and SQLAlchemy session management (`Session`).
- Returns the updated user object according to Pydantic's model schema definition (`response_model`).