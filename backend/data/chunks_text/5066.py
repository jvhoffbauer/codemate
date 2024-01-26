- Defines a fixture named `setup_db` that is available at session scope and automatically called before all tests in this module (autouse).
- Uses SQLAlchemy's engine to drop existing tables and create new ones using Flask-SQLAlchemy's `drop_all` and `create_all`.
- Yields control back to pytest, allowing other fixtures or test functions to run.
- Closes the connection after all tests have finished running.