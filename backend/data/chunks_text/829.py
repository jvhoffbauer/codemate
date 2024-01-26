- Defines a function `run_migrations` that takes no arguments and returns nothing (`None`)
- Imports the built-in module `os` to interact with the operating system
- Prints a message indicating that migrations are being executed using string formatting and f-strings
- Executes an external command ('alembic upgrade head') using the `subprocess.Popen` class in Python's standard library, which is wrapped by the `os.system` method for backward compatibility
- Yields control back to the caller of this coroutine using the `yield from` syntax introduced in PEP 525
- After completing all migration steps, executes another external command ('alembic downgrade base') using `os.system`. This step can be omitted if desired.