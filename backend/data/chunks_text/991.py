- Checks if annotation is a subclass of `BaseModel`, `Mapping`, or `UploadFile`. This covers complex data types like Pydantic models and dictionary-like objects. - Calls another helper function `_annotation_is_sequence()` to check for sequence types like lists and tuples. - Uses the built-in `is_dataclass()` function from Python's dataclasses module to detect whether the annotation is a dataclass object. These checks are combined using logical OR to determine if the annotation is considered "complex".