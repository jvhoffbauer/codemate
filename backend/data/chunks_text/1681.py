- Defines a function `custom_generate_unique_id` that takes an argument `route` of type `APIRoute`.
- Inside the function, it extracts the first tag and name from the given route using the attributes `tags` and `name`, respectively.
- Concatenates them with a hyphen as separator to generate a unique identifier for this specific route. The format is `<first_tag>-<route_name>`.