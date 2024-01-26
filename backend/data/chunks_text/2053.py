- Defines a command named `build_all` using Typer's decorator syntax.
- The function takes no arguments and returns nothing (None).
- It first calls `update_languages()`, which likely updates some language information.
- Deletes the existing site directory (if it exists) without raising an error.
- Retrieves a list of languages to build from `get_lang_paths()`.
- Sets up a process pool with a size based on CPU count and multiplies by 4.
- Uses the `Pool` context manager to map the `build_lang()` function over the list of languages retrieved earlier.