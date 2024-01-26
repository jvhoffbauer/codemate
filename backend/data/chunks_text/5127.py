- Defines a pytest fixture named `set_env` that takes in a `monkeypatch` object as an argument.
- Uses the `monkeypatch` module to set environment variables for AWS access keys, regions, and profile information.
- Deletes the existing `AWS_PROFILE` variable without raising an error (raising=false).
- Sets a non-existent configuration file path to simulate missing config files during testing.