- Defines a function `check_calls` that takes in a list of lists as an argument called `calls`.
- Uses Python's built-in `assert` statement to verify certain conditions about the first three elements (i.e., dictionary objects) within each nested list in `calls`.
- The specific conditions being checked are:
   - For the first element in the first nested list, it should have four key-value pairs with corresponding values for 'name','secret_name', and 'id'. The value for 'age' is optional and can be `None`.
   - For the first element in the second nested list, it should also have four key-value pairs with different values for 'name' and'secret_name'. Again, 'age' is optional.
   - For the first element in the third nested list, all four key-value pairs should be present with unique values for 'name','secret_name', and 'id'. In this case, 'age' has a non-null value of `48`.