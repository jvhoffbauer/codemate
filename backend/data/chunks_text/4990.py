- Defines a class method called `filter` for the current model (specified by `cls`)
- Takes any number of positional arguments and keyword arguments as input
- Returns a queryset containing objects that match the given filters (using Django's built-in `FilterQuerySet` functionality)