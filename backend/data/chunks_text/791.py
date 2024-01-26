- Defines a method `serializable_dict` that returns a dictionary containing only serializable fields of an object's model data.
- Initializes a variable called `default_dict` with the result of calling the `model_dump` function on the current object (presumably to get all its attributes).
- Returns the output of the `jsonable_encoder` function applied to `default_dict`. This likely converts the resulting dictionary into a format suitable for JSON encoding and serialization.