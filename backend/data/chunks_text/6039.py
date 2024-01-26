- Defines a `UserAdmin` subclass of `django_starlette_rest_framework.admin.ModelAdmin`, which registers the `User` model and specifies two fields to display in the list view (ID and username).
- Registers the custom admin with the `AdminSite`.
- Retrieves the created instance of the custom admin for testing purposes.
- Asserts that the 'username' field is included in the schema for the list view.
- Tests the generated OpenAPI documentation by retrieving it from the FastAPI application and checking if the 'username' property exists in the schema for the `UserAdminList` object.