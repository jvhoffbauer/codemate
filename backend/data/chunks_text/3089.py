- Defines a new endpoint `/example/` using FastAPI's decorator syntax
- Accepts an argument named `item`, which is bound to the request body parsed by Pydantic's `Body()` function with a custom model called `Item`. The default value of this parameter is set to an instance of `Item` initialized with a dictionary containing a key-value pair for `data` and a string value of "Data in Body example". This allows us to pass data directly through the request body instead of as query parameters or path variables, making it more flexible and convenient for complex requests.