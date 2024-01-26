- Checks if a given `ModelField` represents a byte sequence by checking its shape (using `sequence_shapes`) and whether it's a subclass of `bytes`. The latter check is done using `lenient_issubclass`, which allows for subclasses that don't inherit directly from `bytes`. This function returns a boolean value indicating whether the field is a byte sequence or not.