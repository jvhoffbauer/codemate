- Tests validation of implicit and explicit `None` values in SQLModel using Pydantic version 1.
- Consistency with Pydantic's behavior where validators are not called for unsupplied arguments.
- Raises a ValidationError when passing an argument with a value of `None`, but allows it if passed as an optional parameter with a default value of `None`.