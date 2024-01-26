1. Creates a new table named 'user' with columns for email, is_active, is_superuser, full_name (optional), hashed_password, and an autoincrementing primary key ('id'). The email column is also indexed as a unique constraint ('ix_user_email').
2. Creates a new table named 'item' with columns for title, description (optional), owner_id (a foreign key referencing the user table's 'id'), and an autoincrementing primary key ('id'). A foreign key constraint links the 'owner_id' column to the corresponding 'id' column in the 'user' table.