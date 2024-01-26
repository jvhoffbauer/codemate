- Defines a function `get_current_user()` that takes an optional OAuth header as input (default value provided by FastAPI's security feature).
- If no OAuth header is present, returns `None`. Otherwise, creates a new `User` object with the username extracted from the header and returns it.