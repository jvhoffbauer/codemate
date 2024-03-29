- Defines a GET request for the path `"/path/param-gt-int"` with an integer parameter named `item_id`.
- The value of `item_id` must be greater than 3, as specified by the `Path` decorator's `gt` argument.
- Returns the value of `item_id`, which will be passed to the function if it meets the constraint defined in the `Path` decorator.