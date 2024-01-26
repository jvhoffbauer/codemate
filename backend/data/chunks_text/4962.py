1. Creates a FastAPI instance with debug mode and customized title/description based on environment variables.
2. Registers database models using `setup_db_models()`.
3. Initializes routes using `setup_routers()`.
4. Configures static file paths using `setup_static_files()`.
5. Sets up global middleware using `setup_middleware()`.
6. Configure logging using `setup_logging()`.
7. Initializes Sentry error tracking (optional).