- Defines a function `read_current_user()` that takes an optional argument `credentials`.
- If no value is provided for `credentials`, it uses the default value of `Security(security)`.
- The function returns an object with two keys -'scheme' and 'credentials', which are extracted from either the passed in `credentials` or the default one obtained using `Security(security)`.