- Tests the background task functionality by making a GET request to `/context_b_bg`.
- Verifies that both contexts A and B are initialized, but the background context is not yet set.
- Asserts that the expected values for contexts A and B are returned in the JSON response.
- Confirms that the final states of contexts A and B are as expected after completing their tasks.
- Checks that the combined string representing all active contexts includes both foreground and background contexts.