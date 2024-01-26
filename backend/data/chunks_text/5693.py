- Defines a class property called `values` that returns a list of all unique values from the choices tuple defined on the same model or base class (cls)
- Uses list comprehension to extract just the first element (value) from each pair in the choices tuple and ignore the second element (_)
- Can be used as an alternative to defining multiple getter methods for individual choice fields