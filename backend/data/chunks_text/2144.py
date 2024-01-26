- Defines a GET route with path parameter `item_id`, which can be passed as a floating point number using Pydantic's `Path()` decorator
- Uses optional query parameters `lt` and `gt` to set lower and upper bounds for the acceptable range of values for `item_id`. These defaults are specified in the function signature (`lt=3` and `gt=1`) but can also be overridden by passing them as URL arguments when making requests (e.g., `http://localhost:8000/path/param-lt-gt/2.5?lt=4&gt=6`)