- Generates a `requirements.txt` file using Pipenv's `lock` command and saves it to the current directory.
- Also generates a separate `requirements-dev.txt` file containing development dependencies, again saved to the current directory.
- Both commands are executed as subprocesses within the context of the script (using `ctx.run()`) rather than being run directly. This allows for more complex setup logic before or after running these commands if needed.