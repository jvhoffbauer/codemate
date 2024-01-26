- This method is a special attribute called `__setattr__`, which allows us to override how object attributes are set.
- It takes two arguments - `key` and `value`. The former represents the name of the attribute being assigned, while the latter holds its new value.
- Inside this function, we're creating a dictionary named `_update` within our class instance (i.e., `self`) that will store all updated keys with their corresponding values.