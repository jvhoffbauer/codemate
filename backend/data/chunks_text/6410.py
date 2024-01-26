- Defines a function `get_data_model` that takes a class as an argument (`cls`)
- Checks whether the given class already has a variable called `data_model`. If it exists, returns it directly. Otherwise...
- Assigns a new value to the `data_model` attribute of the given class using its own `build_data_model` method and saves it for future use by other methods in this class or subclasses inheriting from it.