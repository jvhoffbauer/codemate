- Defines a custom CRUD for SQLAlchemy using `sqlacodegen`'s `SqlalchemyCrud`.
- Sets the prefix and primary key name of the API endpoints.
- Registers the CRUD with the FastAPI application.
- Asserts that the primary key is correctly set to 'username'.
- Makes GET requests to retrieve specific and multiple items by their primary keys ('username').