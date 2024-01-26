- Defines a function `json_request` that takes in another function `raw_request`.
- Inside `json_request`, defines an inner function `requester` which accepts data and optional path postfix as arguments.
- The `requester` makes a JSON request using the `raw_request` provided by calling it with the JSON representation of the input data and optionally appending the given path postfix to the URL.
- Returns the resulting response object from `raw_request` parsed into a dictionary (JSON).