- Tests if passing a decimal value (2.7) as path parameter causes a validation error with status code 422 and appropriate error message from pydantic's IntField.
- Uses `IsDict` type hint for expected JSON response format.
- Includes both current and deprecated error formats in assertion due to backward compatibility requirements.