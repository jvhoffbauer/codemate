- Skips a test if Python version is not 3.8 due to minor marker differences
- Generates temporary output directory for testing purposes
- Creates required files using `pipenv lock` command and saves them in separate directories
- Compares original requirement files with generated ones to ensure they match