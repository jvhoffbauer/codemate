- Creates all tables defined by SQLAlchemy models using SQLite engine and disables automatic schema validation (checkfirst=False).
- Captures standard output from console during execution of above statement.
- Asserts that a specific column definition is present in the created table's CREATE TABLE statement for an enum field type.
- Assertion also checks if any unnecessary CREATE TYPE statements are generated while creating the database schema.