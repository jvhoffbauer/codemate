- Initializes a new instance of the class with an AdminApp object passed as argument to the constructor
- Sets the file directory for storing files using the `or` operator to fallback to the value of `file_path` if it's not defined yet
- Creates the specified directory (if it doesn't already exist) using the `os.makedirs()` function and setting the `exist_ok` flag to True
- Mounts the staticfiles folder by calling the `mount_staticfile()` method inherited from Flask's `Flask` class