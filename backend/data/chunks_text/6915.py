1. Creates a table named 'user' with columns for user ID, full name, email, hashed password, is active flag, and is superuser flag. Primary key constraint set on ID column. Indexes created for email, full name, and ID columns.
2. Creates a table named 'item' with columns for item ID, title, description, and owner ID (foreign key referencing 'user'). Primary key constraint set on ID column. Indexes created for description, title, and ID columns.