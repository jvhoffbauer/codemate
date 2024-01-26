1. Initializes `relationships`, `dict_for_pydantic`, `original_annotations`, `pydantic_annotations`, and `relationship_annotations`.
2. Adds `__weakref__` and `__sqlmodel_relationships__` to `dict_used`.
3. Filters config kwargs using `allowed_config_kwargs` and sets `config_kwargs`.
4. Creates a new instance of the class using `super().__new__()` and passes `dict_used` and `config_kwargs`.
5. Sets `__annotations__` for the new instance using `relationship_annotations`, `pydantic_annotations`, and existing `__annotations__`.
6. Defines a function `get_config()` to retrieve configuration values.
7. Retrieves `config_table` using `get_config()` and sets it as a column attribute for each field.
8. Sets a config flag called `read_from_attributes` to indicate that the object should be read from its attributes rather than being converted into a dictionary.
9. Retrieves `config_registry` using `get_config()` and sets it as a private attribute of the class along with metadata and abstractness flags.