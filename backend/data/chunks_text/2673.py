- Defines a GET endpoint with the given path and returns data in the format of User model, without explicitly specifying its annotations (i.e., no `ResponseModel()` decorator). - The returned value is a custom subclass `DBUser`, which includes additional fields beyond those defined by the base `User` class. This demonstrates how FastAPI can automatically infer the schema from the return type, even when it's not strictly adhering to the declared model structure.