- Generates a new password using `random_lower_string()`.
- Retrieves or creates a user based on their email address in Google Cloud Datastore.
- Updates the user's password (if they already existed).
- Returns an authorization header containing the user's credentials for future requests to the server API.