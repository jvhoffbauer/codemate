- Defines a decorator `ep` that takes an endpoint object as input (`ep`) and returns another function that is also a decorator.
- Inside this inner decorator, it defines a method called `probe`, which takes a parameter `whole_params` of type `WholeParams`. This parameter has default values provided by the `Param` class with ellipsis syntax. The returned value from this method is a list of integers obtained by adding each integer element in `whole_params.data` to its corresponding `amount` property.
- Finally, the outer decorator `ep` returns the inner decorator function.