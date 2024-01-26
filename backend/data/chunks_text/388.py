- Tries to create a SQLAlchemy column for an `id` field in a `Item` model without specifying an index, which raises a `RuntimeError`.
- The error is raised because SQLAlchemy requires that all primary key columns have an index by default.
- This test ensures that FastAPI's ORM extension (SQLModel) correctly handles this scenario and raises the expected exception.