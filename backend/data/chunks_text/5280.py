- Replaces URL with local file path for testing purposes using `DATA_DIR`. - Mocks the behavior of opening a raster dataset from a remote location (URL) to a local one during tests, thanks to the `mock` decorator. - Helps in unit testing by avoiding network requests and ensuring faster test execution times.