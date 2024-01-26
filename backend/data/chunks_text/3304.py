- Defines a function `get2` with an argument `foo`, which is annotated as an integer and has a dependency on `dep`. - The value of `foo` will be automatically injected into the function by Starlette's dependency injection system using the `Depends()` decorator. - This syntax allows for more complex dependencies to be passed in without having to manually manage them within the function body.