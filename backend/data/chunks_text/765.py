- Creates a new table called `auth_user` with columns for user ID (auto-generated, not primary key), email, password, admin status, and creation/update timestamps. Primary key is set to `id`.
- Creates a new table called `auth_refresh_token` with columns for UUID, associated user ID, refresh token, expiration time, and creation/update timestamps. Foreign key links back to `auth_user.id`, deletes related rows when user is deleted. Primary key is set to `uuid`.