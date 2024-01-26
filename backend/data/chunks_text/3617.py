- Defines a function `app_shutdown` that is called when FastAPI receives a shutdown signal (e.g., Ctrl+C or SIGINT). - Sets the value of the global variable `state.app_shutdown` to `True`. This can be used by other parts of the application to perform cleanup tasks before exiting.