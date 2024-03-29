- Retrieves current user from database using JWT token and FastAPI's built-in SQLAlchemy integration
- Decodes JWT token with secret key and checks for validity
- Returns user object or raises error if user is not found in database