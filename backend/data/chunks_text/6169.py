- Defines a function `load` that takes two arguments - `name` (a string representing the filename to be loaded) and optional keyword arguments for JSON loading (passed on to Python's built-in `json.load`)
- Returns either a dictionary or a string depending on whether the file extension is `.json`. In case of `.json`, it calls Python's built-in `json.load` function passing in any additional keyword arguments provided by the user. Otherwise, it simply reads the contents of the file using a context manager and returns them as a string.