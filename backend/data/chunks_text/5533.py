- Retrieves a dictionary of SQLAlchemy's `InstrumentedAttribute` objects from an instance of a subclass of `TableModel`.
- The dictionary is created by iterating over all attributes (keys and values) of the given `TableModel` class, filtering out non-`InstrumentedAttribute` instances using Python's built-in `isinstance()` function, and storing each remaining attribute as key-value pairs in the resulting dictionary.