- Defines an asynchronous function `read_items()` that takes a default argument for `ads_id`, which is set to `Cookie(default=None)`. This allows us to pass in an optional `ads_id` parameter, or use the value stored in a cookie if it exists. - The function returns a dictionary with a key of "ads_id" and its corresponding value from either the input parameter or the cookie (if provided).