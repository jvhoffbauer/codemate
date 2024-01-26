- Defines a fixture named `models` using PyTest's `@pytest.fixture` decorator with parameterized values from the list `models_params_list`.
- The `ids` argument is set to the same value as `params`, which will be used as the identifier for each test case in the output report.
- Returns an imported module object containing SQLAlchemy declarative base classes defined in files within the `tests/models` directory, where the file name corresponds to the requested model class.