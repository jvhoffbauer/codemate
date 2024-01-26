- Creates a directory called `api` using Pytest's temporary file system (`pytester`)
- Copies the contents of either `tests/conftest.py` or `conftest.py` into the new directory
- Generates two Python scripts named `mobile.py` and `web.py`, both containing an example FastAPI JSON RPC endpoint with different entrypoints but identical method signatures