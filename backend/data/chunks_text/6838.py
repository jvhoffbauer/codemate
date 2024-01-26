- This function is a validator for the `EMAILS_FROM_NAME` field in a class using Pydantic's validation decorators (`@validator`)
- It takes two arguments - the value of the `EMAILS_FROM_NAME` field and a dictionary containing all other fields being validated (`values`)
- If `EMAILS_FROM_NAME` is empty or None, it returns the value of the `PROJECT_NAME` field instead