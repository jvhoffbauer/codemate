- Defines a base class for SQLAlchemy's declarative API called `ORMBase`.
- Adds two attributes, `id` and `__name__`, to this base class.
- Uses the `@declared_attr` decorator to generate the `__tablename__` attribute dynamically based on the class name in lowercase format.