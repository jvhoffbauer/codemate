def get_response_text1() -> str:
    python_version = os.getenv("PYTHON_VERSION")
    return f"Hello world! From FastAPI running on Uvicorn with Gunicorn. Using Python {python_version}"