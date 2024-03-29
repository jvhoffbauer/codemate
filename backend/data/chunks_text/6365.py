- Retrieves configuration from a Gunicorn configuration file using `get_gunicorn_conf_path()`.
- Executes the configured Gunicorn command inside a container using `Container.exec_run()`.
- Returns the parsed JSON output of the executed command as a dictionary.