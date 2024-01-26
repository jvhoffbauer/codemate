- Defines a function `lang_callback` that takes an optional string argument `lang`.
- If `lang` is none, returns `None`. Otherwise, checks whether it's a valid ISO 639-1 two-letter language code and raises an error with a message if it isn't.
- Converts the input to lowercase before returning it as a plain string (or `None`) depending on its initial value.