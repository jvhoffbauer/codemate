- Defines a GET route for `"/header_example_examples/"`, which returns a value based on the provided `data`.
- Uses FastAPI's `Header` parameter decorator to define custom headers with defaults and examples.
- The `default` argument sets the initial value of the header if it is not specified in the request. In this case, it is set to `None`.
- The `example` argument provides an example value that will be displayed when generating API documentation using tools like Swagger or ReDoc. Here, we have set it to `"header_overridden"`.
- The `examples` argument allows us to provide multiple examples for the header. These can be used by clients as alternatives to the default value or the `example` value. In our example, we have defined two examples called `"header1"` and `"header2"`.