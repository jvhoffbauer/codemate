- Tests different query parameters for retrieving a list of users from the API endpoint `/User/list`.
- Verifies that all five users are returned when no filters are applied (first call).
- Retrieves user with ID 1 using filter by ID (second call).
- Fetches user with username 'User_1' using filter by username (third call).
- Demonstrates how to use wildcard characters in filters ('[' and ']') to match multiple values or ranges (fourth through seventh calls).
- Shows how to search for users based on partial matches using regular expressions (eighth call).
- Illustrates how to specify date range limits using ISO format strings (ninth call).