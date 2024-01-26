- Defines a dataclass `SelectPerm` with attributes `name`, `label`, and an optional boolean flag `reverse`. - Includes a default value of `False` for `reverse`. - Provides an optional callback function (`call`) that can be assigned to either the constructor or as a separate attribute named `_call`. - Raises an AssertionError if no callback function is provided.