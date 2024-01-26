- Tests validation of implicit and explicit `None` values in SQLModel using Pydantic's `Validator` decorator. - Consistency with Pydantic's behavior where validators are not called for unspecified arguments. - Addresses issues related to handling `None` values in both libraries (#230 for SQLModel, #1223 for Pydantic).